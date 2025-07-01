#include "Common.hpp"

namespace pkpy {

static PythonContext *_pyctx;

PythonContext *pyctx() {
	if (!_pyctx)
		_pyctx = new PythonContext();
	return _pyctx;
}

void py_newvariant(py_OutRef out, const Variant *val) {
	switch (val->get_type()) {
		case Variant::NIL:
			py_newnone(out);
			return;
		case Variant::BOOL:
			py_newbool(out, val->operator bool());
			return;
		case Variant::INT:
			py_newint(out, val->operator int64_t());
			return;
		case Variant::FLOAT:
			py_newfloat(out, val->operator double());
			return;
		case Variant::STRING: {
			auto s = val->operator String();
			py_newstring(out, s);
			return;
		}
		case Variant::VECTOR2:
		case Variant::VECTOR2I:
		case Variant::RECT2:
		case Variant::RECT2I:
		case Variant::VECTOR3:
		case Variant::VECTOR3I:
		case Variant::TRANSFORM2D:
		case Variant::VECTOR4:
		case Variant::VECTOR4I:
		case Variant::PLANE:
		case Variant::QUATERNION:
		case Variant::AABB:
		case Variant::BASIS:
		case Variant::TRANSFORM3D:
		case Variant::PROJECTION:
		case Variant::COLOR:
		case Variant::STRING_NAME:
		case Variant::NODE_PATH:
		case Variant::RID:
		case Variant::OBJECT:
		case Variant::CALLABLE:
		case Variant::SIGNAL:
		case Variant::DICTIONARY:
		case Variant::ARRAY:
		case Variant::PACKED_BYTE_ARRAY:
		case Variant::PACKED_INT32_ARRAY:
		case Variant::PACKED_INT64_ARRAY:
		case Variant::PACKED_FLOAT32_ARRAY:
		case Variant::PACKED_FLOAT64_ARRAY:
		case Variant::PACKED_STRING_ARRAY:
		case Variant::PACKED_VECTOR2_ARRAY:
		case Variant::PACKED_VECTOR3_ARRAY:
		case Variant::PACKED_COLOR_ARRAY:
		case Variant::PACKED_VECTOR4_ARRAY:
		case Variant::VARIANT_MAX: {
			void *ud = py_newobject(out, pyctx()->tp_Variant, 0, sizeof(Variant));
			Variant *v = new (ud) Variant(*val);
			break;
		}
	}
}

void py_newstring(py_OutRef out, String val) {
	auto s = val.utf8();
	c11_sv sv;
	sv.data = s.get_data();
	sv.size = (int)s.length();
	py_newstrv(out, sv);
}

Variant py_tovariant(py_Ref val) {
	switch (py_typeof(val)) {
		case tp_NoneType:
			return Variant();
		case tp_bool:
			return py_tobool(val);
		case tp_int:
			return py_toint(val);
		case tp_float:
			return py_tofloat(val);
		case tp_str: {
			c11_sv sv = py_tosv(val);
			return String::utf8(sv.data, sv.size);
		}
		default: {
			if (py_istype(val, pyctx()->tp_Variant)) {
				void *ud = py_touserdata(val);
				return *static_cast<Variant *>(ud);
			} else {
				return {};
			}
		}
	}
}

void log_python_error_and_clearexc(py_StackRef p0) {
	char *msg = py_formatexc();
	print_error(String(msg));
	PK_FREE(msg);
	py_clearexc(p0);
}

} // namespace pkpy