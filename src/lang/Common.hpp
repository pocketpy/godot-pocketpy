#pragma once

#include "pocketpy.h"
#include <godot_cpp/variant/string_name.hpp>

namespace pkpy {

    inline py_Name godot_name_to_python(godot::StringName name){
        py_Name retval;
        memcpy(&retval, &name, sizeof(py_Name));
        return retval;
    }

    inline godot::StringName python_name_to_godot(py_Name name) {
        godot::StringName retval;
        memcpy(&retval, &name, sizeof(godot::StringName));
        return retval;
    }

} // namespace pkpy