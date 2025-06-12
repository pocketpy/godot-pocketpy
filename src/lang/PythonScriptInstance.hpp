#pragma once

#include <godot_cpp/classes/ref.hpp>
#include <godot_cpp/templates/hash_map.hpp>
#include "pocketpy.h"

using namespace godot;

namespace pkpy {

class PythonScript;

struct PythonScriptInstance {
	PythonScriptInstance(Object *owner, Ref<PythonScript> script);
	~PythonScriptInstance();

	static GDExtensionScriptInstanceInfo3 *get_script_instance_info();
	static PythonScriptInstance *attached_to_object(Object *owner);

	Object *owner;
	Ref<PythonScript> script;
	py_TValue py;

private:
	static HashMap<Object *, PythonScriptInstance *> known_instances;
};

}
