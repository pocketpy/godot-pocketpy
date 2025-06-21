#pragma once

#include "pocketpy.h"

#include <atomic>
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
	py_Type tp_NativeClass;
	py_Type tp_Variant;
	// internals
	py_Type tp_ExportStatement;
	std::thread::id main_thread_id;
	std::atomic_flag lock;
	PythonScriptReloadingContext reloading_context;
};

struct ExportStatement {
	int index;
	String template_;
	StringName name;
	Variant default_value;

	bool operator<(const ExportStatement &other) const {
		return index < other.index;
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

inline void log_python_error_and_clearexc(py_StackRef p0) {
	char *msg = py_formatexc();
	ERR_PRINT(msg);
	PK_FREE(msg);
	py_clearexc(p0);
}

void py_newvariant(py_OutRef out, const Variant *val);
void py_newstring(py_OutRef out, String val);

Variant py_tovariant(py_Ref val);

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