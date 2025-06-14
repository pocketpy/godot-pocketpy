#pragma once

#include "pocketpy.h"

#include <godot_cpp/variant/string_name.hpp>
#include <godot_cpp/variant/variant.hpp>


namespace pkpy {

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

void godot_variant_to_python(py_OutRef out, const godot::Variant *val);
void python_to_godot_variant(godot::Variant *out, py_Ref val);

} // namespace pkpy