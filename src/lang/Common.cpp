#include "Common.hpp"

namespace pkpy {

void godot_variant_to_python(py_OutRef out, const godot::Variant *val) {
	switch (val->get_type()) {
		case godot::Variant::NIL:
			py_newnone(out);
			return;
		case godot::Variant::BOOL:
			py_newbool(out, val->operator bool());
			return;
		case godot::Variant::INT:
			py_newint(out, val->operator int64_t());
			return;
		case godot::Variant::FLOAT:
			py_newfloat(out, val->operator double());
			return;
		case godot::Variant::STRING: {
			auto s = val->operator godot::String().utf8();
			c11_sv sv;
			sv.data = s.get_data();
			sv.size = (int)s.length();
			py_newstrv(out, sv);
			return;
		}
		case godot::Variant::VECTOR2:
		case godot::Variant::VECTOR2I:
		case godot::Variant::RECT2:
		case godot::Variant::RECT2I:
		case godot::Variant::VECTOR3:
		case godot::Variant::VECTOR3I:
		case godot::Variant::TRANSFORM2D:
		case godot::Variant::VECTOR4:
		case godot::Variant::VECTOR4I:
		case godot::Variant::PLANE:
		case godot::Variant::QUATERNION:
		case godot::Variant::AABB:
		case godot::Variant::BASIS:
		case godot::Variant::TRANSFORM3D:
		case godot::Variant::PROJECTION:
		case godot::Variant::COLOR:
		case godot::Variant::STRING_NAME:
		case godot::Variant::NODE_PATH:
		case godot::Variant::RID:
		case godot::Variant::OBJECT:
		case godot::Variant::CALLABLE:
		case godot::Variant::SIGNAL:
		case godot::Variant::DICTIONARY:
		case godot::Variant::ARRAY:
		case godot::Variant::PACKED_BYTE_ARRAY:
		case godot::Variant::PACKED_INT32_ARRAY:
		case godot::Variant::PACKED_INT64_ARRAY:
		case godot::Variant::PACKED_FLOAT32_ARRAY:
		case godot::Variant::PACKED_FLOAT64_ARRAY:
		case godot::Variant::PACKED_STRING_ARRAY:
		case godot::Variant::PACKED_VECTOR2_ARRAY:
		case godot::Variant::PACKED_VECTOR3_ARRAY:
		case godot::Variant::PACKED_COLOR_ARRAY:
		case godot::Variant::PACKED_VECTOR4_ARRAY:
		case godot::Variant::VARIANT_MAX:
			break;
	}
}

void python_to_godot_variant(godot::Variant *out, py_Ref val) {
}

} // namespace pkpy