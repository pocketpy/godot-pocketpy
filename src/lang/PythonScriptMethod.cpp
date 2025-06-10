#include "PythonScriptMethod.hpp"

namespace pkpy {

PythonScriptMethod::PythonScriptMethod(const StringName& name, sol::protected_function method)
	: name(name)
	, method(method)
{
}

bool PythonScriptMethod::is_valid() const {
	return method.valid();
}

int PythonScriptMethod::get_line_defined() const {
	return -1;
}

Variant PythonScriptMethod::get_argument_count() const {
	return {};
}

MethodInfo PythonScriptMethod::to_method_info() const {
	MethodInfo mi;
	mi.name = name;
	return mi;
}

Dictionary PythonScriptMethod::to_dictionary() const {
	return to_method_info();
}

void PythonScriptMethod::register_lua(lua_State *L) {
	
}

}
