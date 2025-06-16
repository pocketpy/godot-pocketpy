#pragma once

#include <godot_cpp/templates/hash_map.hpp>
#include <godot_cpp/templates/vector.hpp>

#include "pocketpy.h"

using namespace godot;

namespace pkpy {

struct PythonScriptMetadata {
	py_Type exposed_type;

	bool is_valid;

	bool is_tool;
	StringName class_name;
	StringName extends;
	String icon_path;

	// HashMap<StringName, PythonScriptMethod> methods;
	// HashMap<StringName, PythonScriptProperty> properties;
	// HashMap<StringName, PythonScriptSignal> signals;

	void setup(py_GlobalRef module);
	PythonScriptMetadata() :
			exposed_type(0), is_valid(false), is_tool(false) {}
};

} //namespace pkpy
