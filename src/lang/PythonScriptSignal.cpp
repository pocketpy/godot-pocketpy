#include "PythonScriptSignal.hpp"

namespace pkpy {

MethodInfo PythonScriptSignal::to_method_info() const {
	MethodInfo mi;
	mi.name = name;
	for (int i = 0; i < arguments.size(); i++) {
		mi.arguments.push_back(PropertyInfo(Variant::Type::NIL, arguments[i]));
	}
	return mi;
}

Dictionary PythonScriptSignal::to_dictionary() const {
	return to_method_info();
}

}
