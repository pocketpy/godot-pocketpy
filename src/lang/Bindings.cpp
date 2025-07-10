#include "Bindings.hpp"
#include "PythonScriptInstance.hpp"

#include <godot_cpp/classes/engine.hpp>
#include <godot_cpp/classes/file_access.hpp>
#include <godot_cpp/classes/node.hpp>
#include <godot_cpp/core/defs.hpp>
#include <godot_cpp/variant/callable.hpp>

namespace pkpy {

void setup_bindings_generated();

static bool Variant_getattribute(py_Ref self, py_Name name) {
	Variant *v = (Variant *)py_touserdata(self);
	if (v->get_type() == Variant::OBJECT) {
		Object *obj = v->operator Object *();
		bool derived_from_Node = obj->is_class("Node");
		if (derived_from_Node && name == py_name("script")) {
			PythonScriptInstance *inst = PythonScriptInstance::attached_to_object(obj);
			if (inst != nullptr) {
				py_assign(py_retval(), &inst->py);
			} else {
				py_newnone(py_retval());
			}
			return true;
		}
	}

	bool r_valid;
	Variant res = v->get_named(python_name_to_godot(name), r_valid);
	if (!r_valid) {
		return AttributeError(self, name);
	}
	py_newvariant(py_retval(), &res);
	return true;
}

static bool Variant_setattribute(py_Ref self, py_Name name, py_Ref value) {
	Variant *v = (Variant *)py_touserdata(self);
	bool r_valid;
	v->set_named(python_name_to_godot(name), py_tovariant(value), r_valid);
	if (!r_valid) {
		return AttributeError(self, name);
	}
	return true;
}

static bool GDNativeClass_getattribute(py_Ref self, py_Name name) {
	StringName clazz = python_name_to_godot((py_Name)py_totrivial(self));
	StringName sn = python_name_to_godot(name);
	bool has_int_const = ClassDB::class_has_integer_constant(clazz, sn);
	if (has_int_const) {
		int64_t int_value = ClassDB::class_get_integer_constant(clazz, sn);
		py_newint(py_retval(), int_value);
		return true;
	}
	return py_exception(tp_AttributeError, "GDNativeClass '%n' has no attribute '%n'",
			godot_name_to_python(clazz), name);
}

static void setup_exports() {
	// export
	pyctx()->tp_ExportStatement = py_newtype("_ExportStatement", tp_object, pyctx()->godot, [](void *ud) {
		ExportStatement *self = (ExportStatement *)ud;
		self->~ExportStatement();
	});

	py_bind(pyctx()->godot, "export(cls, default=None)", [](int argc, py_Ref argv) -> bool {
		auto ctx = &pyctx()->reloading_context;
		StringName type_name;

		if (py_istype(&argv[0], tp_type)) {
			py_Type type = py_totype(&argv[0]);
			switch (type) {
				case tp_int:
					type_name = "int";
					break;
				case tp_float:
					type_name = "float";
					break;
				case tp_bool:
					type_name = "bool";
					break;
				case tp_str:
					type_name = "String";
					break;
				default:
					return TypeError("cannot export type '%t'", type);
			}
		} else if (py_istype(&argv[0], pyctx()->tp_NativeClass)) {
			PY_CHECK_ARG_TYPE(0, pyctx()->tp_NativeClass);
			type_name = python_name_to_godot((py_Name)py_totrivial(&argv[0]));
		} else {
			return TypeError("expected 'type' or 'GDNativeClass', got '%t'", py_typeof(&argv[0]));
		}

		ExportStatement *ud = (ExportStatement *)py_newobject(py_retval(), pyctx()->tp_ExportStatement, 0, sizeof(ExportStatement));
		ud->index = ctx->next_index();
		ud->template_ = "@export var ?: " + type_name;
		ud->default_value = py_tovariant(&argv[1]);
		return true;
	});

	py_bind(pyctx()->godot, "export_range(min, max, step, *extra_hints, default=None)", [](int argc, py_Ref argv) -> bool {
		auto ctx = &pyctx()->reloading_context;
		ExportStatement *ud = (ExportStatement *)py_newobject(py_retval(), pyctx()->tp_ExportStatement, 0, sizeof(ExportStatement));
		ud->index = ctx->next_index();
		Variant min = py_tovariant(&argv[0]);
		Variant max = py_tovariant(&argv[1]);
		Variant step = py_tovariant(&argv[2]);
		bool any_is_float = min.get_type() == Variant::FLOAT || max.get_type() == Variant::FLOAT || step.get_type() == Variant::FLOAT;
		ud->template_ = String("@export_range({0}, {1}, {2}) var ?").format(Array::make(min, max, step));
		ud->default_value = py_tovariant(&argv[4]);
		if (any_is_float && ud->default_value.get_type() == Variant::INT) {
			ud->default_value = (double)ud->default_value;
		}
		return true;
	});
}

void setup_python_bindings() {
	pyctx()->main_thread_id = std::this_thread::get_id();
	pyctx()->lock.clear();
	pyctx()->names.__init__ = py_name("__init__");
	py_callbacks()->gc_mark = PythonScriptInstance::gc_mark_instances;
	py_callbacks()->print = [](const char *msg) {
		String s(msg);
		if (s.ends_with(String("\n"))) {
			s = s.substr(0, s.length() - 1);
		}
		print_line(s);
	};
	py_callbacks()->flush = []() {
		// No-op, Godot's print is already flushed.
	};
	py_callbacks()->importfile = [](const char *path_cstr) -> char * {
		String path = String::utf8(path_cstr);
		path = "res://site-packages/" + path;
		bool exists = FileAccess::file_exists(path);
		if (!exists) {
			return nullptr;
		}
		Ref<FileAccess> file = FileAccess::open(path, FileAccess::ModeFlags::READ);
		if (!file->is_open()) {
			String msg = "cannot open file '" + path + "' when importing '" + path_cstr + "' module";
			ERR_PRINT(msg);
			return nullptr;
		}
		CharString content = file->get_as_text().utf8();
		char *dup = (char *)PK_MALLOC(content.length() + 1);
		memcpy(dup, content.get_data(), content.length());
		dup[content.length()] = '\0';
		return dup;
	};

	py_GlobalRef godot = pyctx()->godot = py_newmodule("godot");

	// Script
	pyctx()->tp_Script = py_newtype("PythonScriptInstance", tp_object, godot, [](void *ud) {
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

	// GDNativeClass
	pyctx()->tp_NativeClass = py_newtype("GDNativeClass", tp_object, godot, NULL);

	py_tphookattributes(pyctx()->tp_NativeClass, GDNativeClass_getattribute, NULL, NULL);

	py_bindmethod(pyctx()->tp_NativeClass, "__call__", [](int argc, py_Ref argv) -> bool {
		PY_CHECK_ARGC(1);
		PY_CHECK_ARG_TYPE(0, pyctx()->tp_NativeClass);
		StringName clazz = python_name_to_godot((py_Name)py_totrivial(argv));
		Object *obj = ClassDB::instantiate(clazz);
		if (!obj) {
			return RuntimeError("failed to instantiate class '%n'", godot_name_to_python(clazz));
		}
		Variant res(obj);
		py_newvariant(py_retval(), &res);
		return true;
	});

	// Extends
	py_bindfunc(godot, "Extends", [](int argc, py_Ref argv) -> bool {
		auto ctx = &pyctx()->reloading_context;
		PY_CHECK_ARGC(1);
		PY_CHECK_ARG_TYPE(0, pyctx()->tp_NativeClass);
		StringName nativeClass = python_name_to_godot((py_Name)py_totrivial(argv));
		ctx->extends = nativeClass;
		py_assign(py_retval(), py_tpobject(pyctx()->tp_Script));
		return true;
	});

	setup_exports();

	// Variant
	py_Type type = pyctx()->tp_Variant = py_newtype("Variant", tp_object, pyctx()->godot, [](void *ud) {
		Variant *v = static_cast<Variant *>(ud);
		v->~Variant();
	});

	py_tphookattributes(type, Variant_getattribute, Variant_setattribute, NULL);

	py_bindmethod(type, "__call__", [](int argc, py_Ref argv) -> bool {
		Variant *self = (Variant *)py_touserdata(&argv[0]);
		if (self->get_type() != Variant::CALLABLE) {
			return TypeError("Variant is not callable");
		}
		Callable callable(*self);
		int64_t args_count = callable.get_argument_count();
		if (args_count >= 0 && args_count != argc - 1) {
			return TypeError("expected %d arguments, got %d", args_count, argc - 1);
		}
		Array godot_args;
		for (int i = 1; i < argc; i++) {
			godot_args.push_back(py_tovariant(&argv[i]));
		}
		Variant res = callable.callv(godot_args);
		py_newvariant(py_retval(), &res);
		return true;
	});

	py_bindmethod(type, "__getitem__", [](int argc, py_Ref argv) -> bool {
		Variant *self = (Variant *)py_touserdata(&argv[0]);
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
		Variant *self = (Variant *)py_touserdata(&argv[0]);
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
		Variant *self = (Variant *)py_touserdata(&argv[0]);
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
		Variant *self = (Variant *)py_touserdata(&argv[0]);
		String type_name = Variant::get_type_name(self->get_type());
		String r = "<godot.Variant " + type_name + ">";
		py_newstring(py_retval(), r);
		return true;
	});

	py_bindmethod(type, "__str__", [](int argc, py_Ref argv) -> bool {
		Variant *self = (Variant *)py_touserdata(&argv[0]);
		py_newstring(py_retval(), self->stringify());
		return true;
	});

#define DEF_UNARY_OP(__name, __op)                                      \
	py_bindmethod(type, __name, [](int argc, py_Ref argv) -> bool {     \
		PY_CHECK_ARGC(1);                                               \
		Variant *self = (Variant *)py_touserdata(&argv[0]);             \
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
		Variant *self = (Variant *)py_touserdata(&argv[0]);             \
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

	setup_bindings_generated();
}

void register_GDNativeClass(const char *name) {
	py_TValue tmp;
	py_Name sn = py_name(name);
	py_newtrivial(&tmp, pyctx()->tp_NativeClass, (py_i64)sn);
	py_setdict(pyctx()->godot, sn, &tmp);
}

void register_GDNativeSingleton(const char *name, Object *obj) {
	Variant v(obj);
	py_OutRef out = py_emplacedict(pyctx()->godot, py_name(name));
	py_newvariant(out, &v);
}

} //namespace pkpy