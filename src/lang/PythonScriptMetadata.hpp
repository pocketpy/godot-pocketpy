#pragma once

#include <godot_cpp/templates/hash_map.hpp>

#include "pocketpy.h"
#include "PythonScriptMethod.hpp"
#include "PythonScriptProperty.hpp"
#include "PythonScriptSignal.hpp"

using namespace godot;

namespace pkpy {

struct PythonScriptMetadata {
	bool is_valid;
	bool is_tool;

	StringName class_name;
	StringName extends;
	String icon_path;

	py_Type type;

	HashMap<StringName, PythonScriptMethod> methods;
	HashMap<StringName, PythonScriptProperty> properties;
	HashMap<StringName, PythonScriptSignal> signals;

	void setup(py_GlobalRef module);
	void clear();
};

}
