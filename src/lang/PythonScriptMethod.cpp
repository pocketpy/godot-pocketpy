#include "PythonScriptMethod.hpp"

namespace pkpy {

PythonScriptMethod::PythonScriptMethod(StringName name)
	: name(name)
{
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

}
