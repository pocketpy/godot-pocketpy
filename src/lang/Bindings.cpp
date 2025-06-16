#include "Common.hpp"
#include "PythonScriptInstance.hpp"
#include "PythonScriptLanguage.hpp"

#include <godot_cpp/core/defs.hpp>

namespace pkpy {

void setup_python_bindings() {
	py_GlobalRef mod = pyctx()->godot = py_newmodule("godot");

	// export
	py_bindfunc(mod, "exposed", [](int argc, py_Ref argv) -> bool {
		PY_CHECK_ARGC(1);
		PY_CHECK_ARG_TYPE(0, tp_type);
		py_setdict(argv, py_name("__exposed__"), py_True());
		return true;
	});

	py_bind(mod, "export(cls, default=None)", [](int argc, py_Ref argv) -> bool {
        auto ctx = &PythonScriptLanguage::get_singleton()->reloading_context;
		return true;
	});

    // Script
	pyctx()->tp_Script = py_newtype("PythonScriptInstance", tp_object, mod, [](void *ud) {
		auto *self = (PythonScriptInstance *)ud;
		self->~PythonScriptInstance();
	});

	py_bindproperty(
			pyctx()->tp_Script, "owner", [](int argc, py_Ref argv) -> bool {
				auto *self = (PythonScriptInstance *)py_touserdata(&argv[0]);
				Variant owner(self->owner);
				py_newvariant(py_retval(), &owner);
				return true;
			},
			NULL);

    // _NativeClass
    pyctx()->tp_NativeClass = py_newtype("_NativeClass", tp_object, mod, [](void *ud) {
        auto *self = (StringName *)ud;
        self->~StringName();
    });

    py_Ref tmp = py_pushtmp();
    StringName* ud = (StringName*)py_newobject(tmp, pyctx()->tp_NativeClass, 0, sizeof(StringName));
    new (ud) StringName("Node");
    py_setdict(mod, py_name("Node"), tmp);
    py_pop();

	// Extends[T]
	pyctx()->tp_ExtendsType = py_newtype("_ExtendsType", tp_object, mod, NULL);
	py_newobject(
			py_emplacedict(mod, py_name("Extends")),
			pyctx()->tp_ExtendsType,
			0, 0);

	py_bindmethod(pyctx()->tp_ExtendsType, "__getitem__", [](int argc, py_Ref argv) -> bool {
		PY_CHECK_ARGC(2);
		PY_CHECK_ARG_TYPE(1, pyctx()->tp_NativeClass);
        StringName* nativeClass = (StringName *)py_touserdata(&argv[1]);
        auto ctx = &PythonScriptLanguage::get_singleton()->reloading_context;
        ctx->extends = *nativeClass;
		py_assign(py_retval(), py_tpobject(pyctx()->tp_Script));
		return true;
	});

	// Variant
	py_Type type = pyctx()->tp_Variant = py_newtype("Variant", tp_object, pyctx()->godot, [](void *ud) {
		Variant *v = static_cast<Variant *>(ud);
		v->~Variant();
	});

	py_bindmethod(type, "__getitem__", [](int argc, py_Ref argv) -> bool {
		auto self = (Variant *)py_touserdata(&argv[0]);
		Variant key = py_tovariant(&argv[1]);
		bool r_valid;
		Variant value = self->get_keyed(key, r_valid);
		if (r_valid) {
			py_newvariant(py_retval(), &value);
			return true;
		}
		return RuntimeError("!r_valid");
	});

	py_bindmethod(type, "__setitem__", [](int argc, py_Ref argv) -> bool {
		auto self = (Variant *)py_touserdata(&argv[0]);
		Variant key = py_tovariant(&argv[1]);
		Variant value = py_tovariant(&argv[2]);
		bool r_valid;
		self->set_keyed(key, value, r_valid);
		if (r_valid) {
			py_newnone(py_retval());
			return true;
		}
		return RuntimeError("!r_valid");
	});

	py_bindmethod(type, "__bool__", [](int argc, py_Ref argv) -> bool {
		auto self = (Variant *)py_touserdata(&argv[0]);
		bool res = self->booleanize();
		py_newbool(py_retval(), res);
		return true;
	});

	py_bindmethod(type, "__hash__", [](int argc, py_Ref argv) -> bool {
		auto self = (Variant *)py_touserdata(&argv[0]);
		py_newint(py_retval(), self->hash());
		return true;
	});

	py_bindmethod(type, "__repr__", [](int argc, py_Ref argv) -> bool {
		auto self = (Variant *)py_touserdata(&argv[0]);
		String type_name = Variant::get_type_name(self->get_type());
		String r = "<godot.Variant " + type_name + ">";
		py_newstring(py_retval(), r);
		return true;
	});

	py_bindmethod(type, "__str__", [](int argc, py_Ref argv) -> bool {
		auto self = (Variant *)py_touserdata(&argv[0]);
		py_newstring(py_retval(), self->stringify());
		return true;
	});

#define DEF_UNARY_OP(__name, __op)                                      \
	py_bindmethod(type, __name, [](int argc, py_Ref argv) -> bool {     \
		PY_CHECK_ARGC(1);                                               \
		auto self = (Variant *)py_touserdata(&argv[0]);                 \
		Variant other;                                                  \
		Variant r_ret;                                                  \
		bool r_valid;                                                   \
		Variant::evaluate(Variant::__op, *self, other, r_ret, r_valid); \
		if (r_valid) {                                                  \
			py_newvariant(py_retval(), &r_ret);                         \
			return true;                                                \
		}                                                               \
		return RuntimeError("!r_valid");                                \
	});

#define DEF_BINARY_OP(__name, __op)                                     \
	py_bindmethod(type, __name, [](int argc, py_Ref argv) -> bool {     \
		PY_CHECK_ARGC(2);                                               \
		auto self = (Variant *)py_touserdata(&argv[0]);                 \
		Variant other = py_tovariant(&argv[1]);                         \
		Variant r_ret;                                                  \
		bool r_valid;                                                   \
		Variant::evaluate(Variant::__op, *self, other, r_ret, r_valid); \
		if (r_valid) {                                                  \
			py_newvariant(py_retval(), &r_ret);                         \
			return true;                                                \
		}                                                               \
		return RuntimeError("!r_valid");                                \
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

} //namespace pkpy