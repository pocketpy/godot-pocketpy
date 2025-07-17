#pragma once

#include "Common.hpp"

using namespace godot;

namespace pkpy {
void setup_python_bindings();

void register_GDNativeClass(Variant::Type type, const char *name);
void register_GDNativeSingleton(const char *name, Object *obj);
void register_GlobalConstant(const char *name, py_i64 value);

bool Variant_getattribute(py_Ref self, py_Name name);
bool Variant_setattribute(py_Ref self, py_Name name, py_Ref value);
bool Variant_getunboundmethod(py_Ref self, py_Name name);
bool GDNativeClass_getattribute(py_Ref self, py_Name name);

bool handle_gde_call_error(GDExtensionCallError error);

inline StringName to_GDNativeClass(py_Ref self) {
	GDNativeClass *p = (GDNativeClass *)py_totrivial(self);
	return python_name_to_godot(p->name);
}

} //namespace pkpy