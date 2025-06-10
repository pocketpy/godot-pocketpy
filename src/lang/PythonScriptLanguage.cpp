#include "PythonScriptLanguage.hpp"

#include <godot_cpp/classes/engine.hpp>
#include <godot_cpp/classes/project_settings.hpp>
#include <godot_cpp/classes/reg_ex.hpp>
#include <godot_cpp/classes/reg_ex_match.hpp>
#include <godot_cpp/classes/resource_loader.hpp>
#include <godot_cpp/variant/dictionary.hpp>
#include <godot_cpp/variant/packed_string_array.hpp>

namespace pkpy {

constexpr char LUA_PATH_SETTING[] = "lua_gdextension/lua_script_language/package_path";
constexpr char LUA_CPATH_SETTING[] = "lua_gdextension/lua_script_language/package_c_path";
constexpr char LUA_CPATH_WINDOWS_SETTING[] = "lua_gdextension/lua_script_language/package_c_path.windows";
constexpr char LUA_CPATH_MACOS_SETTING[] = "lua_gdextension/lua_script_language/package_c_path.macos";

static void add_project_setting(ProjectSettings *project_settings, const String& setting_name, const Variant& initial_value, bool is_basic = false) {
	if (!project_settings->has_setting(setting_name)) {
		project_settings->set_setting(setting_name, initial_value);
	}
	project_settings->set_initial_value(setting_name, initial_value);
	project_settings->set_as_basic(setting_name, is_basic);
}

String PythonScriptLanguage::_get_name() const {
	return "Lua";
}

void PythonScriptLanguage::_init() {
	lua_state.instantiate();
	lua_state->open_libraries();

	// Global script methods LuaScriptInstance::rawget and LuaScriptInstance::rawset
	sol::state_view state = lua_state->get_lua_state();	
	state.registry()["LuaScriptInstance::rawget"] = wrap_function(state, &LuaScriptInstance::rawget);
	state.registry()["LuaScriptInstance::rawset"] = wrap_function(state, &LuaScriptInstance::rawset);

	// Register scripting specific usertypes
	LuaScriptMethod::register_lua(state);
	LuaScriptProperty::register_lua(state);
	LuaScriptSignal::register_lua(state);

	// Register project settings
	ProjectSettings *project_settings = ProjectSettings::get_singleton();
	add_project_setting(project_settings, LUA_PATH_SETTING, "res://?.lua;res://?/init.lua");
	add_project_setting(project_settings, LUA_CPATH_SETTING, "!/?.so;!/loadall.so");
	add_project_setting(project_settings, LUA_CPATH_WINDOWS_SETTING, "!/?.dll;!/loadall.dll");
	add_project_setting(project_settings, LUA_CPATH_MACOS_SETTING, "!/?.dylib;!/loadall.dylib");

	// Apply project settings (package.path, package.cpath)
	lua_state->set_package_path(project_settings->get_setting_with_override(LUA_PATH_SETTING));
	lua_state->set_package_cpath(project_settings->get_setting_with_override(LUA_CPATH_SETTING));
}

String PythonScriptLanguage::_get_type() const {
	return "PythonScript";
}

String PythonScriptLanguage::_get_extension() const {
	return "python";
}

void PythonScriptLanguage::_finish() {
	lua_state.unref();
}

PackedStringArray PythonScriptLanguage::_get_reserved_words() const {
	PackedStringArray reserved_words;
	reserved_words.append_array(get_lua_keywords());
	reserved_words.append_array(get_lua_member_keywords());
	return reserved_words;
}

bool PythonScriptLanguage::_is_control_flow_keyword(const String &keyword) const {
	return godot::helpers::append_all(PackedStringArray(),
		"break", "do", "else", "elseif", "end",
		"for", "goto", "if", "in",
		"repeat", "return",
		"then", "until", "while"
	).has(keyword);
}

PackedStringArray PythonScriptLanguage::_get_comment_delimiters() const {
	return godot::helpers::append_all(PackedStringArray(),
		"--", "--[[ ]]"
	);
}

PackedStringArray PythonScriptLanguage::_get_doc_comment_delimiters() const {
	return godot::helpers::append_all(PackedStringArray(),
		"---"
	);
}

PackedStringArray PythonScriptLanguage::_get_string_delimiters() const {
	return godot::helpers::append_all(PackedStringArray(),
		"' '", "\" \"", "[[ ]]", "[=[ ]=]"
	);
}

Ref<Script> PythonScriptLanguage::_make_template(const String &_template, const String &class_name, const String &base_class_name) const {
	Ref<LuaScript> script = memnew(LuaScript);
	String source_code = _template.replace("_BASE_", base_class_name)
		.replace("_CLASS_", class_name)
		.replace("_TS_", "\t");
	script->set_source_code(source_code);
	return script;
}

TypedArray<Dictionary> PythonScriptLanguage::_get_built_in_templates(const StringName &p_object) const {
#ifdef DEBUG_ENABLED
	Dictionary base_template;
	base_template["inherit"] = "Node";
	base_template["id"] = 0;
	base_template["name"] = "default";
	base_template["description"] = "Default template";
	base_template["origin"] = 0;
	base_template["content"] =
R"(local _CLASS_ = {
_TS_extends = _BASE_,
}

return _CLASS_
)";

	return Array::make(base_template);
#else
	return {};
#endif
}

bool PythonScriptLanguage::_is_using_templates() {
	return true;
}

Dictionary PythonScriptLanguage::_validate(const String &script, const String &path, bool validate_functions, bool validate_errors, bool validate_warnings, bool validate_safe_lines) const {
	Dictionary result;
	Variant f = lua_state->load_string(script, path);
	if (LuaError *error = Object::cast_to<LuaError>(f)) {
		if (validate_errors) {
			Ref<RegEx> line_re = RegEx::create_from_string(R":(\d+):");
			Ref<RegExMatch> match = line_re->search(error->get_message());
			Dictionary error_dict;
			error_dict["path"] = path;
			error_dict["line"] = match->get_string().to_int();
			error_dict["column"] = 1;
			error_dict["message"] = error->get_message();
			result["errors"] = Array::make(error_dict);
		}
		result["valid"] = false;
	}
	else {
		result["valid"] = true;
	}
	return result;
}

String PythonScriptLanguage::_validate_path(const String &path) const {
	return "";
}

Object *PythonScriptLanguage::_create_script() const {
	return memnew(PythonScript);
}

bool PythonScriptLanguage::_has_named_classes() const {
	return false;
}

bool PythonScriptLanguage::_supports_builtin_mode() const {
	return true;
}

bool PythonScriptLanguage::_supports_documentation() const {
	// TODO: does it support documentation?
	return false;
}

bool PythonScriptLanguage::_can_inherit_from_file() const {
	return false;
}

int32_t PythonScriptLanguage::_find_function(const String &p_function, const String &p_code) const {
	// TODO
	return -1;
}

String PythonScriptLanguage::_make_function(const String &p_class_name, const String &p_function_name, const PackedStringArray &p_function_args) const {
	// TODO
	return {};
}

bool PythonScriptLanguage::_can_make_function() const {
	// TODO
	return {};
}

Error PythonScriptLanguage::_open_in_external_editor(const Ref<Script> &p_script, int32_t p_line, int32_t p_column) {
	return OK;
}

bool PythonScriptLanguage::_overrides_external_editor() {
	return false;
}

ScriptLanguage::ScriptNameCasing PythonScriptLanguage::_preferred_file_name_casing() const {
	return SCRIPT_NAME_CASING_AUTO;
}

Dictionary PythonScriptLanguage::_complete_code(const String &p_code, const String &p_path, Object *p_owner) const {
	// TODO
	return {};
}

Dictionary PythonScriptLanguage::_lookup_code(const String &p_code, const String &p_symbol, const String &p_path, Object *p_owner) const {
	// TODO
	Dictionary result;
	result["result"] = ERR_UNAVAILABLE;
	result["type"] = Variant::Type::NIL;
	return result;
}

String PythonScriptLanguage::_auto_indent_code(const String &p_code, int32_t p_from_line, int32_t p_to_line) const {
	// TODO
	return p_code;
}

void PythonScriptLanguage::_add_global_constant(const StringName &p_name, const Variant &p_value) {
	lua_state->get_globals()->set(p_name, p_value);
}

void PythonScriptLanguage::_add_named_global_constant(const StringName &p_name, const Variant &p_value) {
	lua_state->get_globals()->set(p_name, p_value);
}

void PythonScriptLanguage::_remove_named_global_constant(const StringName &p_name) {
	lua_state->get_globals()->set(p_name, nullptr);
}

void PythonScriptLanguage::_thread_enter() {
}

void PythonScriptLanguage::_thread_exit() {
}

String PythonScriptLanguage::_debug_get_error() const {
	// TODO
	return {};
}

int32_t PythonScriptLanguage::_debug_get_stack_level_count() const {
	// TODO
	return {};
}

int32_t PythonScriptLanguage::_debug_get_stack_level_line(int32_t p_level) const {
	// TODO
	return {};
}

String PythonScriptLanguage::_debug_get_stack_level_function(int32_t p_level) const {
	// TODO
	return {};
}

String PythonScriptLanguage::_debug_get_stack_level_source(int32_t p_level) const {
	// TODO
	return {};
}

Dictionary PythonScriptLanguage::_debug_get_stack_level_locals(int32_t p_level, int32_t p_max_subitems, int32_t p_max_depth) {
	// TODO
	return {};
}

Dictionary PythonScriptLanguage::_debug_get_stack_level_members(int32_t p_level, int32_t p_max_subitems, int32_t p_max_depth) {
	// TODO
	return {};
}

void *PythonScriptLanguage::_debug_get_stack_level_instance(int32_t p_level) {
	// TODO
	return {};
}

Dictionary PythonScriptLanguage::_debug_get_globals(int32_t p_max_subitems, int32_t p_max_depth) {
	// TODO
	return {};
}

String PythonScriptLanguage::_debug_parse_stack_level_expression(int32_t p_level, const String &p_expression, int32_t p_max_subitems, int32_t p_max_depth) {
	// TODO
	return {};
}

TypedArray<Dictionary> PythonScriptLanguage::_debug_get_current_stack_info() {
	// TODO
	return {};
}

void PythonScriptLanguage::_reload_all_scripts() {
	// TODO
}

void PythonScriptLanguage::_reload_tool_script(const Ref<Script> &p_script, bool p_soft_reload) {
	// TODO
}


PackedStringArray PythonScriptLanguage::_get_recognized_extensions() const {
	return godot::helpers::append_all(PackedStringArray(),
		"lua"
	);
}

TypedArray<Dictionary> PythonScriptLanguage::_get_public_functions() const {
	// TODO
	return {};
}

Dictionary PythonScriptLanguage::_get_public_constants() const {
	// TODO
	return {};
}

TypedArray<Dictionary> PythonScriptLanguage::_get_public_annotations() const {
	// TODO
	return {};
}

void PythonScriptLanguage::_profiling_start() {
	// TODO
}

void PythonScriptLanguage::_profiling_stop() {
	// TODO
}

void PythonScriptLanguage::_profiling_set_save_native_calls(bool p_enable) {
	// TODO
}

int32_t PythonScriptLanguage::_profiling_get_accumulated_data(ScriptLanguageExtensionProfilingInfo *p_info_array, int32_t p_info_max) {
	// TODO
	return {};
}

int32_t PythonScriptLanguage::_profiling_get_frame_data(ScriptLanguageExtensionProfilingInfo *p_info_array, int32_t p_info_max) {
	// TODO
	return {};
}

void PythonScriptLanguage::_frame() {
}

bool PythonScriptLanguage::_handles_global_class_type(const String &type) const {
	return type == _get_type();
}

Dictionary PythonScriptLanguage::_get_global_class_name(const String &path) const {
	Ref<LuaScript> script = ResourceLoader::get_singleton()->load(path);
	
	Dictionary result;
	if (script.is_valid() && script->_is_valid()) {
		result["name"] = script->_get_global_name();
		result["base_type"] = script->_get_instance_base_type();
		result["icon_path"] = script->_get_class_icon_path();
		result["is_abstract"] = script->_is_abstract();
		result["is_tool"] = script->_is_tool();
	}
	return result;
}

PackedStringArray PythonScriptLanguage::get_lua_keywords() const {
	return godot::helpers::append_all(PackedStringArray(),
		// Lua keywords
		"and", "break", "do", "else", "elseif", "end",
		"false", "for", "function", "goto", "if", "in",
		"local", "nil", "not", "or", "repeat", "return",
		"then", "true", "until", "while"
	);
}

PackedStringArray PythonScriptLanguage::get_lua_member_keywords() const {
	return godot::helpers::append_all(PackedStringArray(),
		// Remarkable identifiers
#if LUA_VERSION_NUM >= 502
		"_ENV",
#endif
		"self", "_G", "_VERSION"
	);
}

LuaState *PythonScriptLanguage::get_lua_state() {
	return lua_state.ptr();
}

PythonScriptLanguage *PythonScriptLanguage::get_singleton() {
	return instance;
}

PythonScriptLanguage *PythonScriptLanguage::get_or_create_singleton() {
	if (!instance) {
		instance = memnew(LuaScriptLanguage);
		Engine::get_singleton()->register_script_language(instance);
	}
	return instance;
}

void PythonScriptLanguage::delete_singleton() {
	if (instance) {
		Engine::get_singleton()->unregister_script_language(instance);
		memdelete(instance);
		instance = nullptr;
	}
}

void PythonScriptLanguage::_bind_methods() {
}

PythonScriptLanguage *PythonScriptLanguage::instance = nullptr;

}
