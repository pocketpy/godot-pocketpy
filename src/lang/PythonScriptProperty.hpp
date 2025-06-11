#pragma once

#include <godot_cpp/core/property_info.hpp>
#include <godot_cpp/variant/variant.hpp>

using namespace godot;

namespace pkpy {

class PythonScriptInstance;

struct PythonScriptProperty {
	Variant::Type type = Variant::NIL;
	StringName name;
	StringName class_name;
	uint32_t hint = PROPERTY_HINT_NONE;
	String hint_string;
	uint32_t usage = PROPERTY_USAGE_SCRIPT_VARIABLE;

	PythonScriptProperty() = default;
	PythonScriptProperty(const Variant& value, const StringName& name);

	Variant default_value;

	StringName getter_name;
	StringName setter_name;

	bool get_value(PythonScriptInstance *self, Variant& r_value) const;
	bool set_value(PythonScriptInstance *self, const Variant& value) const;
	Variant instantiate_default_value() const;

	PropertyInfo to_property_info() const;
	Dictionary to_dictionary() const;
};

}
