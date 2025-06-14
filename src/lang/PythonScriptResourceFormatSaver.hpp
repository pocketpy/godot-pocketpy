#pragma once

#include <godot_cpp/classes/resource_format_saver.hpp>

using namespace godot;

namespace pkpy {

class PythonScriptResourceFormatSaver : public ResourceFormatSaver {
	GDCLASS(PythonScriptResourceFormatSaver, ResourceFormatSaver);

public:
	Error _save(const Ref<Resource> &resource, const String &path, uint32_t flags) override;
	// Error _set_uid(const String &path, int64_t uid) override;
	bool _recognize(const Ref<Resource> &resource) const override;
	PackedStringArray _get_recognized_extensions(const Ref<Resource> &resource) const override;
	// bool _recognize_path(const Ref<Resource> &resource, const String &path) const override;

	static void register_in_godot();
	static void unregister_in_godot();

protected:
	static void _bind_methods();
};

} //namespace pkpy
