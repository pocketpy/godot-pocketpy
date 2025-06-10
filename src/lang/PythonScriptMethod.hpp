#pragma once

#include <godot_cpp/core/object.hpp>

typedef struct lua_State lua_State;

using namespace godot;

namespace pkpy {

struct PythonScriptMethod {
	StringName name;
	sol::protected_function method;
	
	PythonScriptMethod() = default;
	PythonScriptMethod(const StringName& name, sol::protected_function method);

	bool is_valid() const;
	int get_line_defined() const;
	Variant get_argument_count() const;

	MethodInfo to_method_info() const;
	Dictionary to_dictionary() const;

	static void register_lua(lua_State *L);
};

}

#endif  // __LUA_SCRIPT_METHOD_HPP__
