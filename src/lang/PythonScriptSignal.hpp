#pragma once

#include <godot_cpp/core/object.hpp>
#include <godot_cpp/variant/variant.hpp>

typedef struct lua_State lua_State;

using namespace godot;

namespace pkpy {

struct PythonScriptSignal {
	StringName name;
	PackedStringArray arguments;

	MethodInfo to_method_info() const;
	Dictionary to_dictionary() const;

	static void register_lua(lua_State *L);
};

}
