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
			py_newnativefunc(py_retval(), [](int argc, py_Ref argv) {
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
	if (name == pyctx()->names.__name__) {
		py_newstring(py_retval(), String(clazz));
		return true;
	}
	StringName sn = python_name_to_godot(name);
	// const
	bool has_int_const = ClassDB::class_has_integer_constant(clazz, sn);
	if (has_int_const) {
		int64_t int_value = ClassDB::class_get_integer_constant(clazz, sn);
		py_newint(py_retval(), int_value);
		return true;
	}
	return py_exception(tp_AttributeError, "GDNativeClass '%n' has no attribute '%n'",
			godot_name_to_python(clazz), name);
}

bool GDNativeClass_getunboundmethod(py_Ref self, py_Name name) {
	GDNativeClass *p = (GDNativeClass *)py_totrivial(self);
	if (name == pyctx()->names.__call__) {
		py_newnativefunc(py_retval(), [](int argc, py_Ref argv) -> bool {
			GDNativeClass *p = (GDNativeClass *)py_totrivial(argv);
			StringName clazz = python_name_to_godot(p->name);

			if (p->type == Variant::OBJECT) {
				PY_CHECK_ARGC(1);
				if (!ClassDB::can_instantiate(clazz)) {
					return TypeError("cannot instantiate class '%n'", p->name);
				}
				Variant res = ClassDB::instantiate(clazz);
				py_newvariant(py_retval(), &res);
			} else {
				InternalArguments arguments;
				for (int i = 1; i < argc; i++) {
					arguments.append(py_tovariant(&argv[i]));
				}
				Variant r_ret;
				GDExtensionCallError r_error;
				internal::gdextension_interface_variant_construct((GDExtensionVariantType)p->type, &r_ret, arguments.ptr(), arguments.size(), &r_error);
				if (!handle_gde_call_error(r_error)) {
					return false;
				}
				py_newvariant(py_retval(), &r_ret);
			}
			return true;
		});
		return true;
	}
	pythreadctx()->pending_nativecalls.append(std::make_pair(*p, name));
	py_newnativefunc(py_retval(), [](int argc, py_Ref argv) -> bool {
		Vector<std::pair<GDNativeClass, py_Name>> *stack = &pythreadctx()->pending_nativecalls;
		int last_idx = (int)stack->size() - 1;
		std::pair<GDNativeClass, py_Name> pair = stack->operator[](last_idx);
		stack->remove_at(last_idx);

		InternalArguments args;

		Variant r_ret;
		GDExtensionCallError r_error;
		StringName method = python_name_to_godot(pair.second);
		if (pair.first.type == Variant::OBJECT) {
			args.append(python_name_to_godot(pair.first.name));
			args.append(method);
			for (int i = 1; i < argc; i++) {
				args.append(py_tovariant(&argv[i]));
			}
			ClassDBSingleton *singleton = ClassDBSingleton::get_singleton();
			static GDExtensionMethodBindPtr _gde_method_bind = internal::gdextension_interface_classdb_get_method_bind(singleton->get_class_static()._native_ptr(), StringName("class_call_static")._native_ptr(), 3344196419);
			CHECK_METHOD_BIND_RET(_gde_method_bind, (Variant()));
			internal::gdextension_interface_object_method_bind_call(_gde_method_bind, singleton->_owner, args.ptr(), args.size(), &r_ret, &r_error);
		} else {
			for (int i = 1; i < argc; i++) {
				args.append(py_tovariant(&argv[i]));
			}
			godot::internal::gdextension_interface_variant_call_static(
					(GDExtensionVariantType)pair.first.type, &method, args.ptr(), args.size(), &r_ret, &r_error);
		}
		if (!handle_gde_call_error(r_error)) {
			return false;
		}
		py_newvariant(py_retval(), &r_ret);
		return true;
	});
	return true;
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
			return TypeError("GDEXTENSION_CALL_ERROR_TOO_MANY_ARGUMENTS");
		case GDEXTENSION_CALL_ERROR_TOO_FEW_ARGUMENTS:
			return TypeError("GDEXTENSION_CALL_ERROR_TOO_FEW_ARGUMENTS");
		case GDEXTENSION_CALL_ERROR_INSTANCE_IS_NULL:
			return RuntimeError("GDEXTENSION_CALL_ERROR_INSTANCE_IS_NULL");
		case GDEXTENSION_CALL_ERROR_METHOD_NOT_CONST:
			return RuntimeError("GDEXTENSION_CALL_ERROR_METHOD_NOT_CONST");
		default:
			return RuntimeError("GDExtensionCallError: %d", (int)error.error);
	}
}

static bool godot_isinstance_one(py_Ref obj, py_Ref type_obj) {
	if (py_istype(type_obj, tp_type)) {
		return py_isinstance(obj, py_totype(type_obj));
	}
	py_Type t1 = py_typeof(obj);
	py_Type t2 = py_typeof(type_obj);
	if (t1 == pyctx()->tp_Variant && t2 == pyctx()->tp_GDNativeClass) {
		Variant v = to_variant_exact(obj);
		GDNativeClass *p = (GDNativeClass *)py_totrivial(type_obj);
		if (Object *v_obj = v.operator Object *()) {
			return v_obj->is_class(python_name_to_godot(p->name));
		}
		return v.get_type() == p->type;
	}

	const char *t1_name = py_tpname(t1);
	const char *t2_name = py_tpname(t2);
	String error = "godot.isinstance() takes unexpected arguments: ";
	error += t1_name;
	error += " and ";
	error += t2_name;
	WARN_PRINT(error);
	return false;
}

bool godot_isinstance(int argc, py_Ref argv) {
	PY_CHECK_ARGC(2);
	if (py_istuple(py_arg(1))) {
		int length = py_tuple_len(py_arg(1));
		for (int i = 0; i < length; i++) {
			py_Ref item = py_tuple_getitem(py_arg(1), i);
			if (godot_isinstance_one(py_arg(0), item)) {
				py_newbool(py_retval(), true);
				return true;
			}
		}
		py_newbool(py_retval(), false);
		return true;
	}

	py_newbool(py_retval(), godot_isinstance_one(py_arg(0), py_arg(1)));
	return true;
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