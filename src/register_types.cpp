#include "register_types.h"

#include "gdexample.h"

#include <gdextension_interface.h>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/godot.hpp>

#include <lang/PythonScript.hpp>
#include "pocketpy.h"

using namespace godot;
using namespace pkpy;

static void initialize(ModuleInitializationLevel p_level) {
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}

	py_initialize();

	GDREGISTER_RUNTIME_CLASS(GDExample);

	// Python Script Language
	ClassDB::register_abstract_class<PythonScript>();
	ClassDB::register_abstract_class<PythonScriptLanguage>();
	// ClassDB::register_abstract_class<LuaScriptResourceFormatLoader>();
	// ClassDB::register_abstract_class<LuaScriptResourceFormatSaver>();
	// LuaScriptLanguage::get_or_create_singleton();
	// LuaScriptResourceFormatLoader::register_in_godot();
	// LuaScriptResourceFormatSaver::register_in_godot();
}

static void uninitialize(ModuleInitializationLevel p_level) {
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
		return;
	}

	py_finalize();
}

extern "C" {
// Initialization.
GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
	godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

	init_obj.register_initializer(initialize);
	init_obj.register_terminator(uninitialize);
	init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

	return init_obj.init();
}
}