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

static PythonScriptSignal lua_signal(sol::variadic_args arguments) {
	PythonScriptSignal signal = {
		.arguments = VariantArguments(arguments).get_array(),
	};
	return signal;
}

void PythonScriptSignal::register_lua(lua_State *L) {
	sol::state_view state(L);
	state.new_usertype<PythonScriptSignal>(
		"PythonScriptSignal",
		sol::no_construction()
	);
	state.set("signal", &lua_signal);
}

}
