#include "Bindings.hpp"
#include "PythonScriptInstance.hpp"

namespace pkpy {

bool Variant_getattribute(py_Ref self, py_Name name) {
	Variant v = to_variant_exact(self);
	if (v.get_type() == Variant::OBJECT) {
		Object *obj = v.operator Object *();
		if (name == pyctx()->names.script) {
			PythonScriptInstance *inst = PythonScriptInstance::attached_to_object(obj);
			if (inst != nullptr) {
				py_assign(py_retval(), &inst->py);
			} else {
				py_newnone(py_retval());
			}
			return true;
		}
	}

	bool r_valid;
	Variant res = v.get_named(python_name_to_godot(name), r_valid);
	if (!r_valid) {
		return AttributeError(self, name);
	}
	py_newvariant(py_retval(), &res);
	return true;
}

bool Variant_setattribute(py_Ref self, py_Name name, py_Ref value) {
	if (self->extra != Variant::OBJECT) {
		String name = Variant::get_type_name((Variant::Type)self->extra);
		return TypeError("Variant of type '%s' does not support attribute assignment", name.utf8().get_data());
	}
	Variant v = to_variant_exact(self);
	bool r_valid;
	v.set_named(python_name_to_godot(name), py_tovariant(value), r_valid);
	if (!r_valid) {
		return AttributeError(self, name);
	}
	return true;
}

bool Variant_getunboundmethod(py_Ref self, py_Name name) {
	Variant v = to_variant_exact(self);
	StringName name_sn = python_name_to_godot(name);
	bool r_valid;
	Variant res = v.get_named(python_name_to_godot(name), r_valid);
	if (r_valid) {
		if (res.get_type() == Variant::CALLABLE) {
			pythreadctx()->pending_callables.append(res.operator Callable());
			py_newnativefunc(py_retval(), [](int argc, py_Ref argv) -> bool {
				Vector<Callable> *stack = &pythreadctx()->pending_callables;
				Array godot_args;
				for (int i = 1; i < argc; i++) {
					godot_args.push_back(py_tovariant(&argv[i]));
				}
				int last_idx = (int)stack->size() - 1;
				Variant res = stack->operator[](last_idx).callv(godot_args);
				stack->remove_at(last_idx);
				py_newvariant(py_retval(), &res);
				return true;
			});
			return true;
		}
	}
	return false;
}

bool GDNativeClass_getattribute(py_Ref self, py_Name name) {
	StringName clazz = to_GDNativeClass(self);
	StringName sn = python_name_to_godot(name);
	bool has_int_const = ClassDB::class_has_integer_constant(clazz, sn);
	if (has_int_const) {
		int64_t int_value = ClassDB::class_get_integer_constant(clazz, sn);
		py_newint(py_retval(), int_value);
		return true;
	}
	return py_exception(tp_AttributeError, "GDNativeClass '%n' has no attribute '%n'",
			godot_name_to_python(clazz), name);
}

bool handle_gde_call_error(GDExtensionCallError error) {
	if (error.error == GDEXTENSION_CALL_OK) {
		return true;
	}
	switch (error.error) {
		case GDEXTENSION_CALL_ERROR_INVALID_METHOD:
			return RuntimeError("GDEXTENSION_CALL_ERROR_INVALID_METHOD");
		case GDEXTENSION_CALL_ERROR_INVALID_ARGUMENT:
			return ValueError("GDEXTENSION_CALL_ERROR_INVALID_ARGUMENT");
		case GDEXTENSION_CALL_ERROR_TOO_MANY_ARGUMENTS:
		case GDEXTENSION_CALL_ERROR_TOO_FEW_ARGUMENTS:
			return TypeError("expected %d arguments, got %d", error.expected, error.argument);
		case GDEXTENSION_CALL_ERROR_INSTANCE_IS_NULL:
			return RuntimeError("GDEXTENSION_CALL_ERROR_INSTANCE_IS_NULL");
		case GDEXTENSION_CALL_ERROR_METHOD_NOT_CONST:
			return RuntimeError("GDEXTENSION_CALL_ERROR_METHOD_NOT_CONST");
		default:
			return RuntimeError("GDExtensionCallError: %d", (int)error.error);
	}
}

void register_GDNativeClass(Variant::Type type, const char *name) {
	py_TValue tmp;
	py_Name sn = py_name(name);
	GDNativeClass clazz(type, sn);
	py_newtrivial(&tmp, pyctx()->tp_GDNativeClass, &clazz, sizeof(GDNativeClass));
	py_setdict(pyctx()->godot_classes, sn, &tmp);
}

void register_GDNativeSingleton(const char *name, Object *obj) {
	Variant v(obj);
	py_OutRef out = py_emplacedict(pyctx()->godot, py_name(name));
	py_newvariant(out, &v);
}

void register_GlobalConstant(const char *name, py_i64 value) {
	py_TValue tmp;
	py_newint(&tmp, value);
	py_setdict(pyctx()->godot, py_name(name), &tmp);
}

} // namespace pkpy