#pragma once

#include "pocketpy.h"

#include <godot_cpp/variant/string_name.hpp>
#include <godot_cpp/variant/variant.hpp>


namespace pkpy {
	
struct PythonContext {
    py_GlobalRef godot_module;
    py_Type tp_GodotVariant;
};

PythonContext* pyctx();

inline py_Name godot_name_to_python(godot::StringName name) {
	py_Name retval;
	memcpy(&retval, &name, sizeof(py_Name));
	return retval;
}

inline godot::StringName python_name_to_godot(py_Name name) {
	godot::StringName retval;
	memcpy(&retval, &name, sizeof(godot::StringName));
	return retval;
}

inline void raise_python_error() {
	char *msg = py_formatexc();
	ERR_PRINT(msg);
	PK_FREE(msg);
}

void py_newvariant(py_OutRef out, const godot::Variant *val);
void py_newstring(py_OutRef out, godot::String val);

godot::Variant py_tovariant(py_Ref val);
void setup_python_bindings();

} // namespace pkpy