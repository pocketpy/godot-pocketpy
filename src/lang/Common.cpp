#include "Common.hpp"

namespace pkpy {

static PythonContext _pyctx;

PythonContext *pyctx() {
	return &_pyctx;
}

void py_newvariant(py_OutRef out, const godot::Variant *val) {
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
			auto s = val->operator godot::String();
			py_newstring(out, s);
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
		case godot::Variant::VARIANT_MAX: {
			void *ud = py_newobject(out, _pyctx.tp_GodotVariant, 0, sizeof(godot::Variant));
			godot::Variant *v = new (ud) godot::Variant(*val);
			break;
		}
	}
}

void py_newstring(py_OutRef out, godot::String val) {
	auto s = val.utf8();
	c11_sv sv;
	sv.data = s.get_data();
	sv.size = (int)s.length();
	py_newstrv(out, sv);
}

godot::Variant py_tovariant(py_Ref val) {
	switch (py_typeof(val)) {
		case tp_NoneType:
			return {};
		case tp_bool:
			return py_tobool(val);
		case tp_int:
			return py_toint(val);
		case tp_float:
			return py_tofloat(val);
		case tp_str: {
			c11_sv sv = py_tosv(val);
			return godot::String::utf8(sv.data, sv.size);
		}
		default: {
			if (py_istype(val, _pyctx.tp_GodotVariant)) {
				void *ud = py_touserdata(val);
				return *static_cast<godot::Variant *>(ud);
			} else {
				return {};
			}
		}
	}
}

void setup_python_bindings() {
	_pyctx.godot_module = py_newmodule("godot");
	py_Type type = _pyctx.tp_GodotVariant = py_newtype("Variant", tp_object, _pyctx.godot_module, [](void *ud) {
		godot::Variant *v = static_cast<godot::Variant *>(ud);
		v->~Variant();
	});

	py_bindmethod(type, "__getitem__", [](int argc, py_Ref argv) -> bool {
		auto self = (godot::Variant *)py_touserdata(&argv[0]);
		godot::Variant key = py_tovariant(&argv[1]);
		bool r_valid;
		godot::Variant value = self->get_keyed(key, r_valid);
		if (r_valid) {
			py_newvariant(py_retval(), &value);
			return true;
		}
		return RuntimeError("!r_valid");
	});

	py_bindmethod(type, "__setitem__", [](int argc, py_Ref argv) -> bool {
		auto self = (godot::Variant *)py_touserdata(&argv[0]);
		godot::Variant key = py_tovariant(&argv[1]);
		godot::Variant value = py_tovariant(&argv[2]);
		bool r_valid;
		self->set_keyed(key, value, r_valid);
		if (r_valid) {
			py_newnone(py_retval());
			return true;
		}
		return RuntimeError("!r_valid");
	});

	py_bindmethod(type, "__bool__", [](int argc, py_Ref argv) -> bool {
		auto self = (godot::Variant *)py_touserdata(&argv[0]);
		bool res = self->booleanize();
		py_newbool(py_retval(), res);
		return true;
	});

	py_bindmethod(type, "__hash__", [](int argc, py_Ref argv) -> bool {
		auto self = (godot::Variant *)py_touserdata(&argv[0]);
		py_newint(py_retval(), self->hash());
		return true;
	});

	py_bindmethod(type, "__repr__", [](int argc, py_Ref argv) -> bool {
		auto self = (godot::Variant *)py_touserdata(&argv[0]);
		godot::String type_name = godot::Variant::get_type_name(self->get_type());
		godot::String r = "<godot.Variant " + type_name + ">";
		py_newstring(py_retval(), r);
		return true;
	});

	py_bindmethod(type, "__str__", [](int argc, py_Ref argv) -> bool {
		auto self = (godot::Variant *)py_touserdata(&argv[0]);
		py_newstring(py_retval(), self->stringify());
		return true;
	});

#define DEF_UNARY_OP(__name, __op)                                                    \
	py_bindmethod(type, __name, [](int argc, py_Ref argv) -> bool {                   \
		PY_CHECK_ARGC(1);                                                             \
		auto self = (godot::Variant *)py_touserdata(&argv[0]);                        \
		godot::Variant other;                                                         \
		godot::Variant r_ret;                                                         \
		bool r_valid;                                                                 \
		godot::Variant::evaluate(godot::Variant::__op, *self, other, r_ret, r_valid); \
		if (r_valid) {                                                                \
			py_newvariant(py_retval(), &r_ret);                                       \
			return true;                                                              \
		}                                                                             \
		return RuntimeError("!r_valid");                                              \
	});

#define DEF_BINARY_OP(__name, __op)                                                   \
	py_bindmethod(type, __name, [](int argc, py_Ref argv) -> bool {                   \
		PY_CHECK_ARGC(2);                                                             \
		auto self = (godot::Variant *)py_touserdata(&argv[0]);                        \
		godot::Variant other = py_tovariant(&argv[1]);                                \
		godot::Variant r_ret;                                                         \
		bool r_valid;                                                                 \
		godot::Variant::evaluate(godot::Variant::__op, *self, other, r_ret, r_valid); \
		if (r_valid) {                                                                \
			py_newvariant(py_retval(), &r_ret);                                       \
			return true;                                                              \
		}                                                                             \
		return RuntimeError("!r_valid");                                              \
	});

	DEF_BINARY_OP("__eq__", OP_EQUAL)
	DEF_BINARY_OP("__ne__", OP_NOT_EQUAL)
	DEF_BINARY_OP("__lt__", OP_LESS)
	DEF_BINARY_OP("__le__", OP_LESS_EQUAL)
	DEF_BINARY_OP("__gt__", OP_GREATER)
	DEF_BINARY_OP("__ge__", OP_GREATER_EQUAL)

	DEF_BINARY_OP("__add__", OP_ADD)
	DEF_BINARY_OP("__sub__", OP_SUBTRACT)
	DEF_BINARY_OP("__mul__", OP_MULTIPLY)
	DEF_BINARY_OP("__truediv__", OP_DIVIDE)
	DEF_BINARY_OP("__mod__", OP_MODULE)
	DEF_BINARY_OP("__pow__", OP_POWER)
	DEF_BINARY_OP("__lshift__", OP_SHIFT_LEFT)
	DEF_BINARY_OP("__rshift__", OP_SHIFT_RIGHT)
	DEF_BINARY_OP("__and__", OP_BIT_AND)
	DEF_BINARY_OP("__or__", OP_BIT_OR)
	DEF_BINARY_OP("__xor__", OP_BIT_XOR)

	DEF_BINARY_OP("__contains__", OP_IN)
#undef DEF_BINARY_OP

	DEF_UNARY_OP("__neg__", OP_NEGATE)
	// DEF_UNARY_OP("__pos__", OP_POSITIVE)
	DEF_UNARY_OP("__invert__", OP_BIT_NEGATE)
#undef DEF_UNARY_OP
}

} // namespace pkpy