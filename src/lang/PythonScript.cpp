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
#include <thread>

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
	if (!meta.is_valid)
		return StringName();
	return meta.class_name;
}

bool PythonScript::_inherits_script(const Ref<Script> &script) const {
	// if (!meta.is_valid)
	// 	return false;
	// if (const PythonScript *py_script = Object::cast_to<PythonScript>(script.ptr())) {
	// 	py_Type derived = meta.exposed_type;
	// 	py_Type base = py_script->meta.exposed_type;
	// 	if (!derived || !base)
	// 		return false;
	// 	return py_issubclass(derived, base);
	// }
	return false;
}

StringName PythonScript::_get_instance_base_type() const {
	if (!meta.is_valid)
		return StringName();
	return meta.extends;
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
	(void)keep_state;

	PythonContextLock lock;

	printf("=> PythonScript: %p reload from %s\n", this, get_path().utf8().get_data());

	std::thread::id tid = std::this_thread::get_id();
	if (tid != pyctx()->main_thread_id) {
		py_switchvm(0);
	}

	auto ctx = &PythonScriptLanguage::get_singleton()->reloading_context;
	ctx->reset();

	meta.gds.unref();
	meta.class_name = StringName();
	meta.extends = StringName();
	meta.default_values.clear();
	meta.is_valid = false;

	String basename = get_path().get_file().get_basename();
	if (basename.is_empty() || !has_source_code()) {
		return OK;
	}
	auto path_cstr = get_path().utf8();

	printf("==> reloading python script: %s\n", path_cstr.get_data());
	String module_path = "godot.scripts." + basename;
	auto module_path_cstr = module_path.utf8();

	py_GlobalRef module = py_getmodule(module_path_cstr);
	if (module == NULL) {
		module = py_newmodule(module_path_cstr);
	}

	// NOTE: old variables still exist if not overwritten
	bool ok = py_exec(source_code.utf8().get_data(), path_cstr, EXEC_MODE, module);
	if (!ok) {
		raise_python_error();
		return ERR_COMPILATION_FAILED;
	}

	ctx->class_name = StringName(basename);
	py_Name class_name = godot_name_to_python(ctx->class_name);
	py_ItemRef exposed_class = py_getdict(module, class_name);
	if (!exposed_class || !py_istype(exposed_class, tp_type)) {
		ERR_PRINT("Failed to find class '" + ctx->class_name + "' in " + get_path());
		return ERR_COMPILATION_FAILED;
	}

	Vector<ExportStatement> exports;

	ok = py_applydict(
			exposed_class, [](py_Name name, py_ItemRef value, void *ctx) -> bool {
				Vector<ExportStatement> *exports = (Vector<ExportStatement> *)ctx;
				if (py_istype(value, pyctx()->tp_ExportStatement)) {
					ExportStatement *e = (ExportStatement *)py_touserdata(value);
					e->name = python_name_to_godot(name);
					exports->push_back(*e);
				}
				return true;
			},
			&exports);

	if (!ok) {
		raise_python_error();
		return ERR_COMPILATION_FAILED;
	}

	exports.sort();

	PackedStringArray buffer;
	buffer.push_back("# " + get_path());
	buffer.push_back("extends " + ctx->extends);
	buffer.push_back("");
	for (const ExportStatement &e : exports) {
		buffer.push_back(e.template_.replace("?", e.name));
		meta.default_values[e.name] = e.default_value;
	}

	Ref<GDScript> gds = memnew(GDScript);
	meta.gds = gds;
	meta.gds->set_source_code(String("\n").join(buffer));
	Error err = meta.gds->reload(false);
	if (err != OK) {
		// printf("%s\n", meta.gds->get_source_code().utf8().get_data());
		ERR_PRINT("Failed to compile GDScript: " + itos(err));
		return ERR_COMPILATION_FAILED;
	}

	meta.class_name = ctx->class_name;
	meta.extends = ctx->extends;

	meta.is_valid = true;
	return OK;
}

TypedArray<Dictionary> PythonScript::_get_documentation() const {
	// get doc from exposed class
	return {};
}

String PythonScript::_get_class_icon_path() const {
	return String();
}

bool PythonScript::_has_method(const StringName &p_method) const {
	return false;
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
	if (!meta.is_valid)
		return false;
	return meta.gds->is_tool();
}

bool PythonScript::_is_valid() const {
	return meta.is_valid;
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
	return meta.default_values.has(p_property);
}

Variant PythonScript::_get_property_default_value(const StringName &p_property) const {
	if (meta.default_values.has(p_property)) {
		return meta.default_values[p_property];
	}
	return Variant();
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
	auto retval = meta.gds->get_script_property_list();
	if (!retval.is_empty() && retval[0].get("type") == Variant(0)) {
		retval.remove_at(0);
	}
	return retval;
}

int32_t PythonScript::_get_member_line(const StringName &p_member) const {
	return {};
}

Dictionary PythonScript::_get_constants() const {
	return {};
}

TypedArray<StringName> PythonScript::_get_members() const {
	TypedArray<StringName> members;
	TypedArray<Dictionary> properties = get_property_list();
	for (int i = 0; i < properties.size(); i++) {
		members.push_back(properties[i].get("name"));
	}
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

void PythonScript::_bind_methods() {
	ClassDB::bind_vararg_method(METHOD_FLAGS_DEFAULT, "new", &PythonScript::_new);
}

String PythonScript::_to_string() const {
	return String("[%s:%d]") % Array::make(get_class_static(), get_instance_id());
}

static Variant construct_default_variant(Variant::Type type) {
	Variant result;
	GDExtensionCallError error;
	internal::gdextension_interface_variant_construct((GDExtensionVariantType)type, &result, nullptr, 0, &error);
	ERR_FAIL_COND_V_MSG(error.error != GDEXTENSION_CALL_OK, Variant(), "Error constructing " + Variant::get_type_name(type));
	return result;
}

void PythonScript::_update_placeholder_exports(void *placeholder) const {
	Array properties;
	Dictionary default_values;
	TypedArray<Dictionary> raw_properties = _get_script_property_list();
	for (int i = 0; i < raw_properties.size(); i++) {
		properties.append(raw_properties[i]);
		StringName name = raw_properties[i].get("name");
		int type = raw_properties[i].get("type");
		Variant val = _get_property_default_value(name);
		if (val.get_type() == type) {
			default_values[name] = val.duplicate();
		} else {
			default_values[name] = construct_default_variant((Variant::Type)type);
		}
	}
	godot::internal::gdextension_interface_placeholder_script_instance_update(placeholder, properties._native_ptr(), default_values._native_ptr());
}

HashMap<const PythonScript *, HashSet<void *>> PythonScript::placeholders;

} //namespace pkpy
