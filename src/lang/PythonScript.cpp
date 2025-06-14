#include "PythonScript.hpp"

#include "Common.hpp"
#include "PythonScriptInstance.hpp"
#include "PythonScriptLanguage.hpp"

#include "gdextension_interface.h"
#include "godot_cpp/classes/engine.hpp"
#include "godot_cpp/classes/global_constants.hpp"
#include "godot_cpp/core/class_db.hpp"
#include "godot_cpp/core/error_macros.hpp"
#include "godot_cpp/godot.hpp"

#include <stdlib.h>

namespace pkpy {

PythonScript::PythonScript() :
		ScriptExtension() {
	placeholders.insert(this, {});
}

PythonScript::~PythonScript() {
	placeholders.erase(this);
}

bool PythonScript::_editor_can_reload_from_file() {
	return true;
}

void PythonScript::_placeholder_erased(void *p_placeholder) {
	placeholders.get(this).erase(p_placeholder);
}

bool PythonScript::_can_instantiate() const {
	return _is_valid() && (_is_tool() || !Engine::get_singleton()->is_editor_hint());
}

Ref<Script> PythonScript::_get_base_script() const {
	return {};
}

StringName PythonScript::_get_global_name() const {
	return metadata.class_name;
}

bool PythonScript::_inherits_script(const Ref<Script> &script) const {
	if (const PythonScript *py_script = Object::cast_to<PythonScript>(script.ptr())) {
		py_Type derived = metadata.exposed_type;
		py_Type base = py_script->metadata.exposed_type;
		if (!derived || !base)
			return false;
		return py_issubclass(derived, base);
	}
	return false;
}

StringName PythonScript::_get_instance_base_type() const {
	// must return a godot native object
	return metadata.extends;
}

void *PythonScript::_instance_create(Object *for_object) const {
	PythonScriptInstance *instance = memnew(PythonScriptInstance(for_object, Ref<PythonScript>(this)));
	return godot::internal::gdextension_interface_script_instance_create3(PythonScriptInstance::get_script_instance_info(), instance);
}

void *PythonScript::_placeholder_instance_create(Object *for_object) const {
	void *placeholder = godot::internal::gdextension_interface_placeholder_script_instance_create(PythonScriptLanguage::get_singleton()->_owner, this->_owner, for_object->_owner);
	placeholders.get(this).insert(placeholder);
	_update_placeholder_exports(placeholder);
	return placeholder;
}

bool PythonScript::_instance_has(Object *p_object) const {
	return PythonScriptInstance::attached_to_object(p_object);
}

bool PythonScript::_has_source_code() const {
	return !source_code.is_empty();
}

String PythonScript::_get_source_code() const {
	return source_code;
}

void PythonScript::_set_source_code(const String &code) {
	source_code = code;
	_reload(true);
}

Error PythonScript::_reload(bool keep_state) {
	long long rid = get_rid().get_id();
	if (rid == 0) {
		return OK;
	}
	char filename[128];
	snprintf(filename, sizeof(filename), "%lld", rid);
	printf("==> reloading python script: %s\n", filename);
	const char *module_path = filename;
	py_GlobalRef module = py_getmodule(module_path);
	if (module == NULL) {
		module = py_newmodule(module_path);
	}
	// NOTE: old variables still exist if not overwritten
	bool ok = py_exec(source_code.utf8().get_data(), filename, EXEC_MODE, module);
	if (!ok) {
		raise_python_error();
		return ERR_COMPILATION_FAILED;
	}

	ok = py_applydict(
			module, [](py_Name name, py_Ref val, void *ctx) -> bool {
				PythonScriptMetadata *metadata = static_cast<PythonScriptMetadata *>(ctx);
				const char *name_cstr = py_name2str(name);
				if (py_istype(val, tp_type)) {
					py_Type type = py_totype(val);
					// @exposed will set `__exposed__` flag
					bool is_exposed = py_getdict(py_tpobject(type), py_name("__exposed__"));
					if (is_exposed) {
						// setup metadata
						metadata->exposed_type = type;

						while (type) {
							py_GlobalRef typeobject = py_tpobject(type);
							int attrs_length;
							py_Name *attrs = py_tpclassattrs(type, &attrs_length);
							for (int i = 0; i < attrs_length; ++i) {
								py_Name name = attrs[i];
								py_ItemRef val = py_getdict(typeobject, name);
							}
							type = py_tpbase(type);
						}
					}
				}
				return true;
			},
			&metadata);
	return ok ? OK : ERR_COMPILATION_FAILED;
}

TypedArray<Dictionary> PythonScript::_get_documentation() const {
	return {};
}

String PythonScript::_get_class_icon_path() const {
	return metadata.icon_path;
}

bool PythonScript::_has_method(const StringName &p_method) const {
	String name = p_method;
	py_Ref method = py_tpfindname(metadata.exposed_type, godot_name_to_python(p_method));
	return py_callable(method);
}

bool PythonScript::_has_static_method(const StringName &p_method) const {
	return _has_method(p_method); // TODO: check @staticmethod
}

Variant PythonScript::_get_script_method_argument_count(const StringName &p_method) const {
	return {};
}

Dictionary PythonScript::_get_method_info(const StringName &p_method) const {
	return {};
}

bool PythonScript::_is_tool() const {
	return metadata.is_tool;
}

bool PythonScript::_is_valid() const {
	return metadata.is_valid;
}

bool PythonScript::_is_abstract() const {
	return false;
}

ScriptLanguage *PythonScript::_get_language() const {
	return PythonScriptLanguage::get_singleton();
}

bool PythonScript::_has_script_signal(const StringName &p_signal) const {
	return false;
}

TypedArray<Dictionary> PythonScript::_get_script_signal_list() const {
	TypedArray<Dictionary> signals;
	return signals;
}

bool PythonScript::_has_property_default_value(const StringName &p_property) const {
	return false;
}

Variant PythonScript::_get_property_default_value(const StringName &p_property) const {
	return {};
}

void PythonScript::_update_exports() {
	for (void *placeholder : placeholders.get(this)) {
		_update_placeholder_exports(placeholder);
	}
}

TypedArray<Dictionary> PythonScript::_get_script_method_list() const {
	TypedArray<Dictionary> methods;
	return methods;
}

TypedArray<Dictionary> PythonScript::_get_script_property_list() const {
	TypedArray<Dictionary> list;
	return list;
}

int32_t PythonScript::_get_member_line(const StringName &p_member) const {
	return {};
}

Dictionary PythonScript::_get_constants() const {
	return {};
}

TypedArray<StringName> PythonScript::_get_members() const {
	TypedArray<StringName> members;
	return members;
}

bool PythonScript::_is_placeholder_fallback_enabled() const {
	return placeholder_fallback_enabled;
}

Variant PythonScript::_get_rpc_config() const {
	return {};
}

Variant PythonScript::_new(const Variant **args, GDExtensionInt arg_count, GDExtensionCallError &error) {
	printf("==> PythonScript::_new called with %d args\n", (int)arg_count);
	if (!_can_instantiate()) {
		error.error = GDEXTENSION_CALL_ERROR_INVALID_METHOD;
		return {};
	}
	Variant object = ClassDB::instantiate(_get_instance_base_type());
	if (Object *obj = object) {
		obj->set_script(this);
	}
	return object;
}

const PythonScriptMetadata &PythonScript::get_metadata() const {
	return metadata;
}

void PythonScript::_bind_methods() {
	ClassDB::bind_vararg_method(METHOD_FLAGS_DEFAULT, "new", &PythonScript::_new);
}

String PythonScript::_to_string() const {
	return String("[%s:%d]") % Array::make(get_class_static(), get_instance_id());
}

void PythonScript::_update_placeholder_exports(void *placeholder) const {
	Array properties;
	Dictionary default_values;
	godot::internal::gdextension_interface_placeholder_script_instance_update(placeholder, properties._native_ptr(), default_values._native_ptr());
}

HashMap<const PythonScript *, HashSet<void *>> PythonScript::placeholders;

} //namespace pkpy
