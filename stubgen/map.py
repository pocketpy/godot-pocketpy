from typing import NamedTuple
from .schema_gdt import *
from .schema_py import *
from collections import namedtuple

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






# ===============================
# 通用映射
# ===============================

def _map_properties(cls_data: ClassesSingle|BuiltinClass, pyclass: PyClass) -> None:
    """映射实例属性/成员变量"""
    
    for member_data in cls_data.properties or []:
        pyclass.members.append(PyMember(
            name=member_data.name,
            type_expr=PyTypeExpr(
                type=PyType.get(member_data.type),
                expr=member_data.type,
            ),
            inline_comment=member_data.description,
        ))

def _map_methods(cls_data: ClassesSingle|BuiltinClass, pyclass: PyClass) -> None:
    """映射方法，包括普通方法和静态方法"""
    for method_data in cls_data.methods or []:
        description = []
        if method_data.description:
            description.append(method_data.description)
        if description:
            description = '"""' + "\n".join(description) + "\n" + '"""'
            description = description.splitlines()
        pyclass.methods.append(PyMethod(
            name=method_data.name,
            description_lines=description,
            arguments=[],
            vararg_position=None if not method_data.is_vararg else len(method_data.arguments),
            return_value=PyValueExpr(
                expr=method_data.return_value.type,
                type_expr=PyTypeExpr(
                    type=PyType.get(method_data.return_value.type),
                    expr=method_data.return_value.type,
                ),
            ) if method_data.return_value else None,
            is_static=method_data.is_static,
        ))
        
        _map_method_arguments(method_data, pyclass.methods[-1])

def _map_method_arguments(method_data, pymethod: PyMethod) -> None:
    """映射方法参数"""
    for argument_data in method_data.arguments or []:
        pymethod.arguments.append(PyArgument(
            name=argument_data.name,
            type_expr=PyTypeExpr(
                type=PyType.get(argument_data.type),
                expr=argument_data.type,
            ),
            default_value=PyValueExpr(
                expr=argument_data.default_value,
                type_expr=PyTypeExpr(
                    type=PyType.get(argument_data.type),
                    expr=argument_data.type,
                ),
            ) if argument_data.default_value else None,
        ))

def _map_constants(cls_data: ClassesSingle|BuiltinClass, pyclass: PyClass) -> None:
    """映射类常量/类属性"""
    for class_attribute_data in cls_data.constants or []:
        pyclass.members.append(
            PyMember(
                name=class_attribute_data.name,
                type_expr=PyTypeExpr(
                    type=PyType.get('int'),
                    expr=str(class_attribute_data.value),
                ),
                value_expr=PyValueExpr(
                    expr=str(class_attribute_data.value),
                    type_expr=PyTypeExpr(
                        type=PyType.get('int'),
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
    for signal_data in cls_data.signals or []:
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
        replaced_description = signal_data.description.replace('\n', '    ')
        signal_desc = f"{comment} - {replaced_description}" if replaced_description else comment
        pyclass.members.append(PyMember(
            name=signal_data.name,
            type_expr=PyTypeExpr(
                type=None,  # 信号类型是复合类型，不在 type_map 中
                expr=signal_type_expr,
            ),
            inline_comment=signal_desc
        ))
        
def _map_operators(cls_data: BuiltinClass, pyclass: PyClass) -> None:
    """映射运算符重载"""
    for operator_data in cls_data.operators or []:
        if PyMethod.try_parse_name(operator_data.name):
            if operator_data.right_type:
                # 二元运算符（如 __add__、__sub__ 等），有 right_type
                pyclass.methods.append(PyMethod(
					name=PyMethod.OPERATORS_TABLE[operator_data.name],
					arguments=[PyArgument(
					name=operator_data.right_type,
					type_expr=PyTypeExpr(
						type=PyType.get(operator_data.right_type),
						expr=operator_data.right_type,
						),
					)],
					return_value=PyValueExpr(
						expr=operator_data.return_type,
						type_expr=PyTypeExpr(
							type=PyType.get(operator_data.return_type),
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
                            type=PyType.get(operator_data.return_type),
                            expr=operator_data.return_type,
                        ),
                    ),
                    description_lines=operator_data.description.splitlines(),
                ))
        else:
            raise Exception(f"发现新的运算符: {operator_data.name}")

def _map_enum(enum_data: GlobalEnum|ClassesEnum, pyclass: PyClass) -> None:
    """映射枚举"""
    for enum_value_data in enum_data.values or []:
        pyclass.members.append(PyMember(
            name=enum_value_data.name,
            type_expr=PyTypeExpr(
                type=PyType.get('int'),
                expr='int',
            ),
            value_expr=PyValueExpr(
                expr=str(enum_value_data.value),
                type_expr=PyTypeExpr(
                    type=PyType.get('int'),
                    expr='int',
                ),
            ),
            inline_comment=enum_value_data.description,
        ))

# ===============================
# 入口
# ===============================

@dataclass
class MapResult:
    typings_pyi: PyFile
    enum_pyi: PyFile
    init_pyi: PyFile
    
    
def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> MapResult:
    PyType.build_type_map(gdt_all_in_one)
    
    map_result = MapResult(
        typings_pyi=PyFile(
            name="typings.pyi",
            imports=[
            '''from typing import Callable'''
            ],
            classes=[],
        ),
        enum_pyi=PyFile(
            name="enum.pyi",
            imports=[
            '''from enum import Enum'''
            ],
            classes=[],
        ),
        init_pyi=PyFile(
            name="__init__.pyi",
            imports=[
            'from . import typings as _typings',
            '',
            '',
            'class GDNativeSingleton[T: Object]:',
            '    def __init__(self, name: str): ...',
            '',
            'class GDNativeClass[T: Object]:',
            '    def __init__(self, name: str): ...',
            '',
            'class Script[T: Object]:',
            '    @property',
            '        def owner(self) -> T: ...',
            '',
            'def Extends[T: Object](cls: GDNativeClass[T]) -> type[Script[T]]: ...',
            ],
            global_variables=[
            ]
        ),
    )
    
    
    # class single
    class_single_classes = []
    for cls_data in gdt_all_in_one.classes:
        
        description = []
        if cls_data.brief_description:
            description.append(cls_data.brief_description)
        if cls_data.description:
            description.append(cls_data.description)
        if description:
            description = '"""' + "\n".join(description) + "\n" + '"""'
            description = description.splitlines()
        
        pyclass = PyClass(
            type=PyType.get(cls_data.name),
            description_lines = description,
            members = [],
            class_attributes = [],
            methods = [],
        )
        
        # 处理各种属性
        _map_properties(cls_data, pyclass)
        _map_methods(cls_data, pyclass)
        _map_constants(cls_data, pyclass)
        _map_signals(cls_data, pyclass)
        
        class_single_classes.append(pyclass)
    
    # builtin class
    builtin_classes = []
    for cls_data in gdt_all_in_one.builtin_classes:
        description = []
        if cls_data.brief_description:
            description.append(cls_data.brief_description)
        if cls_data.description:
            description.append(cls_data.description)
        if description:
            description = '"""' + "\n".join(description) + "\n" + '"""'
            description = description.splitlines()
        
        pyclass = PyClass(
            type=PyType.get(cls_data.name),
            description_lines=description,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        # 处理各种属性
        _map_methods(cls_data, pyclass)
        _map_constants(cls_data, pyclass)
        _map_operators(cls_data, pyclass)
        
        builtin_classes.append(pyclass)
    
    # enum
    folded_enums = [gdt_all_in_one.global_enums] + [cls_data.enums for cls_data in gdt_all_in_one.classes]
    flattened_enums = [item for sublist in folded_enums for item in sublist]
    
    enum_classes = []
    for enum_data in flattened_enums:
        description = []
        if enum_data.description:
            description.append(enum_data.description)
        if description:
            description = '"""' + "\n" + "\n".join(description) + "\n" + '"""'
            description = description.splitlines()
            
        pyclass = PyClass(
            type=PyType.get(enum_data.name),
            description_lines=description,
            members=[],
            class_attributes=[],
            methods=[],
        )
        
        # 处理各种属性
        _map_enum(enum_data, pyclass)
        enum_classes.append(pyclass)
    
    map_result.enum_pyi.classes.extend(enum_classes)
    
    
    # __init__.pyi
    #
    #   Resource = GDNativeClass[_typings.Resource]('Resource')
    #   Engine = GDNativeSingleton[_typings.Engine]('Engine')
    for pytype in PyType.ALL_TYPES:
        if pytype.category == PyTypeCategory.SINGLETON_GODOT_NATIVE:
            map_result.init_pyi.global_variables.append(PyMember(
                specified_string=f'{pytype.name} = GDNativeSingleton[_typings.{pytype.name}](\'{pytype.name}\')',
            ))
        elif pytype.category == PyTypeCategory.GODOT_NATIVE:
            map_result.init_pyi.global_variables.append(PyMember(
                specified_string=f'{pytype.name} = GDNativeClass[_typings.{pytype.name}](\'{pytype.name}\')',
            ))
    
    # enum.pyi
    for enum_class in enum_classes:
        map_result.enum_pyi.classes.append(enum_class)
    
    # typings.pyi
    for class_single_class in class_single_classes:
        map_result.typings_pyi.classes.append(class_single_class)
    
    for builtin_class in builtin_classes:
        map_result.typings_pyi.classes.append(builtin_class)
    
    
    return map_result