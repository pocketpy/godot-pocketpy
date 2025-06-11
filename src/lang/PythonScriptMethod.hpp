#pragma once

#include <godot_cpp/core/object.hpp>

typedef struct lua_State lua_State;

using namespace godot;

namespace pkpy {

struct PythonScriptMethod {
	StringName name;

	PythonScriptMethod(StringName name);

	int get_line_defined() const;
	Variant get_argument_count() const;
	MethodInfo to_method_info() const;
	Dictionary to_dictionary() const;
};

}

