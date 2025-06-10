#include <godot_cpp/classes/ref_counted.hpp>
#include <godot_cpp/core/class_db.hpp>

#include "PythonScriptMetadata.hpp"

namespace pkpy {

void PythonScriptMetadata::setup(py_GlobalRef module) {
	is_valid = true;

	bool ok = py_applydict(module, [](py_Name name, py_GlobalRef val, void *ctx) -> bool {
		PythonScriptMetadata* meta = static_cast<PythonScriptMetadata*>(ctx);
	}, this);

	// 	String name = key.as<String>();
	// 	if (name == "extends") {
	// 		StringName extends = to_variant(value);
	// 		if (!ClassDB::class_exists(extends)) {
	// 			WARN_PRINT(String("Specified base class '%s' does not exist, using RefCounted") % Array::make(extends));
	// 		}
	// 		else {
	// 			base_class = extends;
	// 		}
	// 	}
	// 	else if (name == "class_name") {
	// 		class_name = to_variant(value);
	// 	}
	// 	else if (name == "icon") {
	// 		icon_path = to_variant(value);
	// 	}
	// 	else if (name == "tool") {
	// 		is_tool = to_variant(value).booleanize();
	// 	}
	// 	else if (auto signal = value.as<sol::optional<LuaScriptSignal>>()) {
	// 		signal->name = name;
	// 		signals.insert(name, *signal);
	// 	}
	// 	else if (auto property = value.as<sol::optional<LuaScriptProperty>>()) {
	// 		property->name = name;
	// 		properties.insert(name, *property);
	// 	}
	// 	else if (value.get_type() == sol::type::function) {
	// 		methods.insert(name, LuaScriptMethod(name, value));
	// 	}
	// 	else {
	// 		Variant var = to_variant(value);
	// 		properties.insert(name, LuaScriptProperty(var, name));
	// 	}

	// 	lua_pop(L, 1);
	// }
}

void PythonScriptMetadata::clear() {
	is_valid = false;
	is_tool = false;
	base_class = RefCounted::get_class_static();
	class_name = StringName();
	icon_path = String();
	properties.clear();
	signals.clear();
	methods.clear();
}

}
