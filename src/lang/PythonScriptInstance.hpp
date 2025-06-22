#pragma once

#include "PythonScript.hpp"
#include "pocketpy.h"
#include <godot_cpp/classes/ref.hpp>
#include <godot_cpp/templates/hash_map.hpp>

using namespace godot;

namespace pkpy {

struct PythonScriptInstance {
	PythonScriptInstance(Object *owner, const PythonScript* script);
	~PythonScriptInstance();

	static GDExtensionScriptInstanceInfo3 *get_script_instance_info();
	static PythonScriptInstance *attached_to_object(Object *owner);

	Object *owner;
	const PythonScript* script;
	py_TValue py;

	static void gc_mark_instances(void (*f)(py_Ref val, void *ctx), void *ctx);

private:
	static HashMap<Object *, PythonScriptInstance *> known_instances;
};

} //namespace pkpy
