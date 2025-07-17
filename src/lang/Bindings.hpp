#pragma once

#include "Common.hpp"

using namespace godot;

namespace pkpy {
void setup_python_bindings();

void register_GDNativeClass(Variant::Type type, const char *name);
void register_GDNativeSingleton(const char *name, Object *obj);
void register_GlobalConstant(const char *name, py_i64 value);

bool handle_gde_call_error(GDExtensionCallError error);

} //namespace pkpy