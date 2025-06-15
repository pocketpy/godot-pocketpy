#include <godot_cpp/classes/ref_counted.hpp>
#include <godot_cpp/core/class_db.hpp>

#include "PythonScriptMetadata.hpp"

namespace pkpy {

void PythonScriptMetadata::setup(py_GlobalRef module) {
	is_valid = true;

	// bool ok = py_applydict(
	// 		module, [](py_Name name, py_GlobalRef val, void *ctx) -> bool {
	// 			PythonScriptMetadata *meta = static_cast<PythonScriptMetadata *>(ctx);
	// 			return true;
	// 		},
	// 		this);
}

} //namespace pkpy
