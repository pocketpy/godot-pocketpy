#include <godot_cpp/classes/script.hpp>

#include "PythonScriptInstance.hpp"

#include "Common.hpp"
#include "PythonScript.hpp"
#include "PythonScriptLanguage.hpp"

namespace pkpy {

PythonScriptInstance::PythonScriptInstance(Object *owner, Ref<PythonScript> script) :
		owner(owner), script(script) {
	known_instances.insert(owner, this);
}

PythonScriptInstance::~PythonScriptInstance() {
	known_instances.erase(owner);
}

GDExtensionBool set_func(PythonScriptInstance *p_instance, const StringName *p_name, const Variant *p_value) {
	bool is_defined = false;
	if (is_defined) {
		py_StackRef p0 = py_peek(0);
		py_StackRef tmp = py_pushtmp();
		py_newvariant(tmp, p_value);
		bool ok = py_setattr(&p_instance->py, godot_name_to_python(*p_name), tmp);
		if (ok) {
			py_pop();
		} else {
			log_python_error_and_clearexc(p0);
		}
		return true;
	} else {
		return false;
	}
}

GDExtensionBool get_func(PythonScriptInstance *p_instance, const StringName *p_name, Variant *p_value) {
	bool is_defined = false;
	if (is_defined) {
		py_StackRef p0 = py_peek(0);
		bool ok = py_getattr(&p_instance->py, godot_name_to_python(*p_name));
		if (ok) {
			*p_value = py_tovariant(py_retval());
		} else {
			log_python_error_and_clearexc(p0);
			*p_value = Variant();
		}
		return true;
	} else {
		return false;
	}
}

GDExtensionScriptInstanceGetPropertyList get_property_list_func;
GDExtensionScriptInstanceFreePropertyList2 free_property_list_func;
GDExtensionScriptInstanceGetClassCategory get_class_category_func;

GDExtensionBool property_can_revert_func(PythonScriptInstance *p_instance, const StringName *p_name) {
	return false;
}

GDExtensionBool property_get_revert_func(PythonScriptInstance *p_instance, const StringName *p_name, Variant *r_ret) {
	*r_ret = {};
	return false;
}

Object *get_owner_func(PythonScriptInstance *p_instance) {
	return p_instance->owner;
}

void get_property_state_func(PythonScriptInstance *p_instance, GDExtensionScriptInstancePropertyStateAdd p_add_func, void *p_userdata) {
	// for (Variant key : *p_instance->data.ptr()) {
	// 	StringName name = key;
	// 	Variant value = p_instance->data->get(key);
	// 	p_add_func(&name, &value, p_userdata);
	// }
	StringName name = "x";
	Variant value = 42;
	p_add_func(&name, &value, p_userdata);
}

GDExtensionScriptInstanceGetMethodList get_method_list_func;
GDExtensionScriptInstanceFreeMethodList2 free_method_list_func;

GDExtensionVariantType get_property_type_func(PythonScriptInstance *p_instance, const StringName *p_name, GDExtensionBool *r_is_valid) {
	if (*p_name == StringName("x")) {
		*r_is_valid = true;
		return GDEXTENSION_VARIANT_TYPE_INT;
	}
	*r_is_valid = false;
	return GDEXTENSION_VARIANT_TYPE_NIL;
}

GDExtensionBool validate_property_func(PythonScriptInstance *p_instance, GDExtensionPropertyInfo *p_property) {
	return true;
}

GDExtensionBool has_method_func(PythonScriptInstance *p_instance, const StringName *p_name) {
	return p_instance->script->_has_method(*p_name);
}

GDExtensionInt get_method_argument_count_func(PythonScriptInstance *p_instance, const StringName *p_name, GDExtensionBool *r_is_valid) {
	Variant result = p_instance->script->_get_script_method_argument_count(*p_name);
	*r_is_valid = result.get_type() != Variant::Type::NIL;
	return result;
}

void call_func(PythonScriptInstance *p_instance, const StringName *p_method, const Variant **p_args, GDExtensionInt p_argument_count, Variant *r_return, GDExtensionCallError *r_error) {
	py_StackRef p0 = py_peek(0);
	py_push(&p_instance->py);
	py_pushmethod(godot_name_to_python(*p_method));
	for (GDExtensionInt i = 0; i < p_argument_count; ++i) {
		py_StackRef arg = py_pushtmp();
		py_newvariant(arg, p_args[i]);
	}
	bool ok = py_vectorcall((uint16_t)p_argument_count, 0);
	if (ok) {
		*r_return = py_tovariant(py_retval());
		r_error->error = GDEXTENSION_CALL_OK;
	} else {
		log_python_error_and_clearexc(p0);
		r_error->error = GDEXTENSION_CALL_ERROR_INVALID_METHOD;
	}
}

void notification_func(PythonScriptInstance *p_instance, int32_t p_what, GDExtensionBool p_reversed) {
}

void to_string_func(PythonScriptInstance *p_instance, GDExtensionBool *r_is_valid, String *r_out) {
	py_StackRef p0 = py_peek(0);
	bool ok = py_repr(&p_instance->py);
	if (ok) {
		*r_is_valid = true;
		c11_sv sv = py_tosv(py_retval());
		*r_out = String::utf8(sv.data, sv.size);
	} else {
		*r_is_valid = false;
		*r_out = String();
		log_python_error_and_clearexc(p0);
	}
}

void refcount_incremented_func(PythonScriptInstance *) {
}

GDExtensionBool refcount_decremented_func(PythonScriptInstance *) {
	return true;
}

void *get_script_func(PythonScriptInstance *instance) {
	return instance->script.ptr()->_owner;
}

GDExtensionBool is_placeholder_func(PythonScriptInstance *instance) {
	return false;
}

GDExtensionScriptInstanceSet set_fallback_func;
GDExtensionScriptInstanceGet get_fallback_func;

void *get_language_func(PythonScriptInstance *instance) {
	return PythonScriptLanguage::get_singleton()->_owner;
}

void free_func(PythonScriptInstance *instance) {
	memdelete(instance);
}

GDExtensionScriptInstanceInfo3 script_instance_info = {
	(GDExtensionScriptInstanceSet)set_func,
	(GDExtensionScriptInstanceGet)get_func,
	(GDExtensionScriptInstanceGetPropertyList)get_property_list_func,
	(GDExtensionScriptInstanceFreePropertyList2)free_property_list_func,
	(GDExtensionScriptInstanceGetClassCategory)get_class_category_func,
	(GDExtensionScriptInstancePropertyCanRevert)property_can_revert_func,
	(GDExtensionScriptInstancePropertyGetRevert)property_get_revert_func,
	(GDExtensionScriptInstanceGetOwner)get_owner_func,
	(GDExtensionScriptInstanceGetPropertyState)get_property_state_func,
	(GDExtensionScriptInstanceGetMethodList)get_method_list_func,
	(GDExtensionScriptInstanceFreeMethodList2)free_method_list_func,
	(GDExtensionScriptInstanceGetPropertyType)get_property_type_func,
	(GDExtensionScriptInstanceValidateProperty)validate_property_func,
	(GDExtensionScriptInstanceHasMethod)has_method_func,
	(GDExtensionScriptInstanceGetMethodArgumentCount)get_method_argument_count_func,
	(GDExtensionScriptInstanceCall)call_func,
	(GDExtensionScriptInstanceNotification2)notification_func,
	(GDExtensionScriptInstanceToString)to_string_func,
	(GDExtensionScriptInstanceRefCountIncremented)refcount_incremented_func,
	(GDExtensionScriptInstanceRefCountDecremented)refcount_decremented_func,
	(GDExtensionScriptInstanceGetScript)get_script_func,
	(GDExtensionScriptInstanceIsPlaceholder)is_placeholder_func,
	(GDExtensionScriptInstanceSet)set_fallback_func,
	(GDExtensionScriptInstanceGet)get_fallback_func,
	(GDExtensionScriptInstanceGetLanguage)get_language_func,
	(GDExtensionScriptInstanceFree)free_func,
};
GDExtensionScriptInstanceInfo3 *PythonScriptInstance::get_script_instance_info() {
	return &script_instance_info;
}

PythonScriptInstance *PythonScriptInstance::attached_to_object(Object *owner) {
	if (PythonScriptInstance **ptr = known_instances.getptr(owner)) {
		return *ptr;
	} else {
		return nullptr;
	}
}

HashMap<Object *, PythonScriptInstance *> PythonScriptInstance::known_instances;

} //namespace pkpy
