#pragma once

#include <godot_cpp/classes/editor_plugin.hpp>
#include <godot_cpp/classes/editor_interface.hpp>
#include <godot_cpp/classes/control.hpp>
#include "PythonScript.hpp"

using namespace godot;

namespace pkpy {

class PythonEditorPlugin : public EditorPlugin {
    GDCLASS(PythonEditorPlugin, EditorPlugin);

    static void _bind_methods() {
        ClassDB::bind_method(D_METHOD("rebuild_index_file"), &PythonEditorPlugin::rebuild_index_file);
    }

    void rebuild_index_file() {
        PythonScript::rebuild_index_file();
    }

public:

#define TOOL_ITEM_NAME "Python: Rebuild Scripts Index File"
    void _enter_tree() override {
		Callable callable(this, "rebuild_index_file");
		add_tool_menu_item(TOOL_ITEM_NAME, callable);
    }

    void _exit_tree() override {
        remove_tool_menu_item(TOOL_ITEM_NAME);
    }
#undef TOOL_ITEM_NAME
};

}