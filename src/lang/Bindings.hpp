#pragma once

#include "Common.hpp"

using namespace godot;

namespace pkpy {
void setup_python_bindings();

void register_GDNativeClass(const char *name);
void register_GDNativeSingleton(const char *name, Object *obj);

} //namespace pkpy