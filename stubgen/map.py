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

OPERATORS_TABLE = {
    '<': '__lt__',
    '<=': '__le__',
    '>': '__gt__',
    '>=': '__ge__',
    '==': '__eq__',
    '!=': '__ne__',
    '+': '__add__',
    '-': '__sub__',
    '*': '__mul__',
    '/': '__truediv__',
    '%': '__mod__',
    '**': '__pow__',
    '<<': '__lshift__',
    '>>': '__rshift__',
    '&': '__and__',
    '|': '__or__',
    '^': '__xor__',
    "in": "__contains__",

    'unary-': '__neg__',
    
    '~': '__invert__',
}

NOT_SUPPORTED_OPERATORS = {
    'unary+': '__pos__',
    'not': '__invert__',
    'and': '__and__',
    'or': '__or__',
    'xor': '__xor__',
}



def _build_type_map(gdt_all_in_one: GodotInOne) -> dict[str, PyType]:
    pytypes = {}
    
    for builtin_class in gdt_all_in_one.builtin_classes:
        pytypes[builtin_class.name] = PyType(
            name=builtin_class.name,
            category=PyTypeCategory.BUILTIN_CLASS,
        )
    
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
        
    for singleton_data in gdt_all_in_one.singletons:
        pytypes[singleton_data.name] = PyType(
            name=singleton_data.name,
            category=PyTypeCategory.SINGLETON,
        )
    
    for enum_data in gdt_all_in_one.global_enums:
        pytypes[enum_data.name] = PyType(
            name=enum_data.name,
            category=PyTypeCategory.ENUM,
        )
    
    # inherits
    for cls_data in gdt_all_in_one.classes:
        if cls_data.inherits:
            pytypes[cls_data.name].inherit = pytypes[cls_data.inherits]
    
    
    return pytypes

def map_gdt_to_py(gdt_all_in_one: GodotInOne) -> list[PyFile]:
    pyfiles = []
    
    type_map = _build_type_map(gdt_all_in_one)
    

    for cls_data in gdt_all_in_one.classes:
        pyclass = PyClass(
            type=type_map[cls_data.name],
            description_lines = ('"""' + cls_data.brief_description + "\n" + cls_data.description + "\n" + '"""').splitlines(),
            members = [],
            class_attributes = [],
            methods = [],
        )
        
        for member_data in cls_data.properties:
            pyclass.members.append(PyMember(
                name=member_data.name,
                type_expr=PyTypeExpr(
                    type=type_map.get(member_data.type),
                    expr=member_data.type,
                ),
                inline_comment=member_data.description,
            ))
        
        for method_data in cls_data.methods:
            pyclass.methods.append(PyMethod(
                name=method_data.name,
                description_lines=method_data.description.splitlines(),
                arguments=[],
                vararg_position=None if not method_data.is_vararg else len(method_data.arguments),
                return_value=PyValueExpr(
                    value_expr=method_data.return_value,
                    type_expr=PyTypeExpr(
                        type=type_map[method_data.return_type],
                        expr=method_data.return_type,
                    ),
                ) if method_data.return_value else None,
                is_static=method_data.is_static,
            ))
            
            for argument_data in method_data.arguments:
                pyclass.methods[-1].arguments.append(PyArgument(
                    name=argument_data.name,
                    type_expr=PyTypeExpr(
                        type=type_map[argument_data.type],
                        expr=argument_data.type,
                    ),
                    default_value=PyValueExpr(
                        value_expr=argument_data.default_value,
                        type_expr=PyTypeExpr(
                            type=type_map[argument_data.type],
                            expr=argument_data.type,
                        ),
                    ) if argument_data.default_value else None,
                ))
                
    
    
    
    
    return pyfiles