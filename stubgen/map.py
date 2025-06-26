from .schema_gdt import *
from .schema_py import *

'''
Node本身的实际类型是GDNativeClass

Node.new()，实际上是调用了GDNativeClass的实例方法new()，这里是类型对象模式


* typings
  * godot
    * `__init__.pyi`，放类的真正定义Resource = GDNativeClass\[godot.typings.Resource\]('Resource')
    * `typings.pyi`，放类型注释
    * `enum.pyi`，放枚举的定义


```python


class GDNativeClass[T: Object]:
    def __init__(self, name: str): ...

class Script[T: Object]:
    @property
    def owner(self) -> T: ...

def Extends[T: Object](cls: GDNativeClass[T]) -> type[Script[T]]: ...

Resource = GDNativeClass[godot.typings.Resource]('Resource')

class MyClass(Extends(Resource)):
    pass

s = MyClass().owner
```

## 重要内容！！

```python
from typing import Literal
GDNativeClass = Literal['Node', 'Node2D', ...]
BuiltinClass = Literal['int', 'float', 'bool', ...]

def Extends(cls: GDNativeClass): ...

def export(cls: GDNativeClass | BuiltinClass): ...

class MyScript(Extends('Node')):
    export_category("Main Category")
    number: int = export('int')
    resource: Resource = export('Resource')
    my_node: Node = export('Node')

    export_group("MyGroup")
    x_int: int = export_range(1, 10, 2)
    x_float: float = export_range(1.0, 10, 2)

    export_subgroup("Extra Properties")
    y_int: int = export('int', default=5)
    z_float: float = export('float', default=3.14)
```


'''





def _build_type_map(gdt_all_in_one: GodotInOne) -> dict[str, PyType]:
    pytypes = {}
    
    for singleton_data in gdt_all_in_one.singletons:
        pytypes[singleton_data.name] = PyType(
            name=singleton_data.name,
            category=PyTypeCategory.SINGLETON,
        )
        PyType.add_singleton_type(pytypes[singleton_data.name])
    
    for builtin_class in gdt_all_in_one.builtin_classes:
        pytypes[builtin_class.name] = PyType(
            name=builtin_class.name,
            category=PyTypeCategory.BUILTIN_CLASS,
        )
        if pytypes[builtin_class.name] not in PyType.SINGLETON_TYPES:
            PyType.add_not_singleton_type(pytypes[builtin_class.name])
    
    for cls_data in gdt_all_in_one.classes:
        
        pytypes[cls_data.name] = PyType(
            name=cls_data.name,
            category=PyTypeCategory.CLASS,
        )
        
        for enum_data in cls_data.enums:
            pytypes[f"{cls_data.name}_{enum_data.name}"] = PyType(
                name=f"{cls_data.name}_{enum_data.name}",
                category=PyTypeCategory.ENUM,
            )
            if pytypes[f"{cls_data.name}_{enum_data.name}"] not in PyType.SINGLETON_TYPES:
                PyType.add_not_singleton_type(pytypes[f"{cls_data.name}_{enum_data.name}"])
                
        if pytypes[cls_data.name] not in PyType.SINGLETON_TYPES:
            PyType.add_not_singleton_type(pytypes[cls_data.name])

    
    for enum_data in gdt_all_in_one.global_enums:
        pytypes[enum_data.name] = PyType(
            name=enum_data.name,
            category=PyTypeCategory.ENUM,
        )
        if pytypes[enum_data.name] not in PyType.SINGLETON_TYPES:
            PyType.add_not_singleton_type(pytypes[enum_data.name])

    # inherits
    for cls_data in gdt_all_in_one.classes:
        if cls_data.inherits:
            pytypes[cls_data.name].inherit = pytypes[cls_data.inherits]
    
    
    return pytypes



# ===============================
# 通用映射
# ===============================

def _map_properties(cls_data: ClassesSingle|BuiltinClass, type_map: dict[str, PyType], pyclass: PyClass) -> None:
    """映射实例属性/成员变量"""
    for member_data in cls_data.properties:
        pyclass.members.append(PyMember(
            name=member_data.name,
            type_expr=PyTypeExpr(
                type=type_map.get(member_data.type),
                expr=member_data.type,
            ),
            inline_comment=member_data.description,
        ))

def _map_methods(cls_data: ClassesSingle|BuiltinClass, type_map: dict[str, PyType], pyclass: PyClass) -> None:
    """映射方法，包括普通方法和静态方法"""
    for method_data in cls_data.methods:
        pyclass.methods.append(PyMethod(
            name=method_data.name,
            description_lines=method_data.description.splitlines(),
            arguments=[],
            vararg_position=None if not method_data.is_vararg else len(method_data.arguments),
            return_value=PyValueExpr(
                expr=method_data.return_value.type,
                type_expr=PyTypeExpr(
                    type=type_map[method_data.return_value.type],
                    expr=method_data.return_value.type,
                ),
            ) if method_data.return_value else None,
            is_static=method_data.is_static,
        ))
        
        _map_method_arguments(method_data, type_map, pyclass.methods[-1])

def _map_method_arguments(method_data, type_map: dict[str, PyType], pymethod: PyMethod) -> None:
    """映射方法参数"""
    for argument_data in method_data.arguments:
        pymethod.arguments.append(PyArgument(
            name=argument_data.name,
            type_expr=PyTypeExpr(
                type=type_map[argument_data.type],
                expr=argument_data.type,
            ),
            default_value=PyValueExpr(
                expr=argument_data.default_value,
                type_expr=PyTypeExpr(
                    type=type_map[argument_data.type],
                    expr=argument_data.type,
                ),
            ) if argument_data.default_value else None,
        ))

def _map_constants(cls_data: ClassesSingle|BuiltinClass, type_map: dict[str, PyType], pyclass: PyClass) -> None:
    """映射类常量/类属性"""
    for class_attribute_data in cls_data.constants:
        pyclass.members.append(
            PyMember(
                name=class_attribute_data.name,
                type_expr=PyTypeExpr(
                    type=type_map['int'],
                    expr=str(class_attribute_data.value),
                ),
                value_expr=PyValueExpr(
                    expr=str(class_attribute_data.value),
                    type_expr=PyTypeExpr(
                        type=type_map['int'],
                        expr=str(class_attribute_data.value),
                    ),
                ),
            )
        )


# ===============================
# 各自独有的映射
# ===============================

def _map_signals(cls_data: ClassesSingle, pyclass: PyClass) -> None:
    """映射信号（特殊类型的类属性）"""
    for signal_data in cls_data.signals:
        # 创建信号类型表达式
        arg_types = []
        arg_comments = []
        
        for arg in signal_data.arguments:
            arg_types.append(arg.type)
            arg_comments.append(f"{arg.name}: {arg.type}")
        
        # 创建信号类型表达式
        signal_type_expr = f"Signal[Callable[[{', '.join(arg_types)}], None]]"
        comment = f"{signal_data.name}({', '.join(arg_comments)})"
        
        # 添加信号成员
        pyclass.members.append(PyMember(
            name=signal_data.name,
            type_expr=PyTypeExpr(
                type=None,  # 信号类型是复合类型，不在 type_map 中
                expr=signal_type_expr,
            ),
            inline_comment=comment if not signal_data.description else f"{comment} - {signal_data.description.replace('\n', '    ')}",
        ))
        
def _map_operators(cls_data: BuiltinClass, type_map: dict[str, PyType], pyclass: PyClass) -> None:
    """映射运算符重载"""
    for operator_data in cls_data.operators:
        if PyMethod.try_parse_name(operator_data.name):
            if operator_data.right_type:
                # 二元运算符（如 __add__、__sub__ 等），有 right_type
                pyclass.methods.append(PyMethod(
					name=PyMethod.OPERATORS_TABLE[operator_data.name],
					arguments=[PyArgument(
					name=operator_data.right_type,
					type_expr=PyTypeExpr(
						type=type_map[operator_data.right_type],
						expr=operator_data.right_type,
						),
					)],
					return_value=PyValueExpr(
						expr=operator_data.return_type,
						type_expr=PyTypeExpr(
							type=type_map[operator_data.return_type],
							expr=operator_data.return_type,
						),
					),
					description_lines=operator_data.description.splitlines(),
				))
            else:
                # 一元运算符（如 __neg__、__invert__ 等），没有 right_type
                pyclass.methods.append(PyMethod(
                    name=PyMethod.OPERATORS_TABLE[operator_data.name],
                    arguments=[],
                    return_value=PyValueExpr(
                        expr=operator_data.return_type,
                        type_expr=PyTypeExpr(
                            type=type_map[operator_data.return_type],
                            expr=operator_data.return_type,
                        ),
                    ),
                    description_lines=operator_data.description.splitlines(),
                ))
        else:
            raise Exception(f"发现新的运算符: {operator_data.name}")

# ===============================
# 入口
# ===============================

def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> list[PyFile]:
    pyfiles = []
    
    type_map = _build_type_map(gdt_all_in_one)
    
    # class single
    for cls_data in gdt_all_in_one.classes:
        pyclass = PyClass(
            type=type_map[cls_data.name],
            description_lines = ('"""' + cls_data.brief_description + "\n" + cls_data.description + "\n" + '"""').splitlines(),
            members = [],
            class_attributes = [],
            methods = [],
        )
        
        # 处理各种属性
        _map_properties(cls_data, type_map, pyclass)
        _map_methods(cls_data, type_map, pyclass)
        _map_constants(cls_data, type_map, pyclass)
        _map_signals(cls_data, pyclass)
    
    # builtin class
    for cls_data in gdt_all_in_one.builtin_classes:
        pyclass = PyClass(
            type=type_map[cls_data.name],
            description_lines=('"""' + cls_data.brief_description + "\n" + cls_data.description + "\n" + '"""').splitlines(),
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        # 处理各种属性
        _map_methods(cls_data, type_map, pyclass)
        _map_constants(cls_data, type_map, pyclass)
        _map_operators(cls_data, type_map, pyclass)
    
    # 单例
    for singleton in gdt_all_in_one.singletons:
            type_map[singleton.type]
        
        
    return pyfiles