#include "register_types.h"

#include <gdextension_interface.h>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/godot.hpp>

#include "lang/PythonScript.hpp"
#include "pocketpy.h"

using namespace godot;
using namespace pkpy;

static void initialize(ModuleInitializationLevel p_level) {
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}

	printf("==> initializing pocketpy...\n");

	py_initialize();

	printf("==> registering pocketpy classes...\n");

	ClassDB::register_abstract_class<PythonScript>();
	ClassDB::register_abstract_class<PythonScriptLanguage>();
	PythonScriptLanguage::get_or_create_singleton();
}

static void uninitialize(ModuleInitializationLevel p_level) {
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}

	printf("==> resetting pocketpy...\n");
	py_resetallvm();
}

extern "C" {
// Initialization.
GDExtensionBool GDE_EXPORT godot_pocketpy_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
	godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

	init_obj.register_initializer(initialize);
	init_obj.register_terminator(uninitialize);
	init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

	return init_obj.init();
}
}