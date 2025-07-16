#pragma once

#include "pocketpy.h"

#include <atomic>
#include <godot_cpp/classes/engine.hpp>
#include <godot_cpp/classes/node.hpp>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/variant/string_name.hpp>
#include <godot_cpp/variant/variant.hpp>
#include <thread>

using namespace godot;

namespace pkpy {

struct PythonScriptReloadingContext {
	StringName class_name;
	StringName extends;
	int counter;

	PythonScriptReloadingContext() :
			class_name(), extends(), counter(0) {}

	inline void reset() {
		class_name = StringName();
		extends = StringName();
		counter = 0;
	}

	inline int next_index() {
		return counter++;
	}
};

struct PythonContext {
	py_GlobalRef godot;
	py_Type tp_Script;
	py_Type tp_GDNativeClass;
	py_Type tp_Variant;
	// internals
	py_Type tp_DefineStatement;
	std::thread::id main_thread_id;
	std::atomic_flag lock;
	PythonScriptReloadingContext reloading_context;
	struct {
		py_Name __init__;
		py_Name script;
	} names;
};

struct GDNativeClass {
	Variant::Type type;
	StringName name;

	GDNativeClass(Variant::Type type, StringName clazz) :
			type(type), name(clazz) {}
};

class UninitializedVariant {
	alignas(8) char data[sizeof(Variant)];

public:
	~UninitializedVariant() {
		((Variant *)data)->~Variant();
	}

	Variant *ptr() {
		return (Variant *)data;
	}
};

struct DefineStatement {
	int index;
	String name;

	DefineStatement(int index) :
			index(index), name() {}

	bool operator<(const DefineStatement &other) const {
		return index < other.index;
	}

	virtual bool is_signal() const = 0;
	virtual ~DefineStatement() = default;
};

struct ExportStatement : DefineStatement {
	String template_;
	Variant default_value;

	using DefineStatement::DefineStatement;

	bool is_signal() const override {
		return false;
	}
};

struct SignalStatement : DefineStatement {
	PackedStringArray arguments;

	using DefineStatement::DefineStatement;

	bool is_signal() const override {
		return true;
	}
};

PythonContext *pyctx();

inline py_Name godot_name_to_python(StringName name) {
	const py_Name &retval = (const py_Name &)name;
	return retval;
}

inline StringName python_name_to_godot(py_Name name) {
	const StringName &sn = (const StringName &)name;
	return sn;
}

void log_python_error_and_clearexc(py_StackRef p0);

void py_newvariant(py_OutRef out, const Variant *val);
void py_newstring(py_OutRef out, String val);

Variant py_tovariant(py_Ref val);
Variant to_variant_exact(py_Ref val);

struct PythonContextLock {
	PythonContextLock() {
		while (pyctx()->lock.test_and_set()) {
			std::this_thread::yield();
		}
	}

	~PythonContextLock() {
		pyctx()->lock.clear();
	}
};

} // namespace pkpy