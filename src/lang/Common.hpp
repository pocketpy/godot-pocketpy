#pragma once

#include "pocketpy.h"

#include <godot_cpp/variant/string_name.hpp>
#include <godot_cpp/variant/variant.hpp>

using namespace godot;

namespace pkpy {

struct PythonContext {
	py_GlobalRef godot;
	py_Type tp_Script;
	py_Type tp_NativeClass;
	py_Type tp_ExtendsType;
	py_Type tp_Variant;
};

PythonContext *pyctx();

inline py_Name godot_name_to_python(StringName name) {
	py_Name retval;
	memcpy(&retval, &name, sizeof(py_Name));
	return retval;
}

inline StringName python_name_to_godot(py_Name name) {
	StringName retval;
	memcpy(&retval, &name, sizeof(StringName));
	return retval;
}

inline void raise_python_error() {
	char *msg = py_formatexc();
	ERR_PRINT(msg);
	PK_FREE(msg);
}

void py_newvariant(py_OutRef out, const Variant *val);
void py_newstring(py_OutRef out, String val);

Variant py_tovariant(py_Ref val);

} // namespace pkpy