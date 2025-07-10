from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Dict, List, Literal, Optional, Set, Any, TypeVar, Union
from functools import cached_property

from ..tools import ValidatorResults


@dataclass
class PyType:
    """一个Python类型"""
    name: str
    inherit: Optional['PyType'] = None
    
    # 类型查找映射
    ALL_TYPES: ClassVar[Dict[str, 'PyType']] = {}
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PyType):
            return False
        return self.name == other.name


@dataclass
class PyTypeExpr:
    """Python类型表达式，可以是单一类型、联合类型等"""
    # 类型表达式字符串
    expr_str: str
    
    # 缓存
    ALL_TYPE_EXPRS: ClassVar[Dict[str, 'PyTypeExpr']] = {}
    
    def __hash__(self) -> int:
        return hash(self.expr_str)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PyTypeExpr):
            return False
        return self.expr_str == other.expr_str


@dataclass
class PyValueExpr:
    """Python值表达式，如字面量值"""
    value_expr: str
    type_expr: Optional[PyTypeExpr] = None


@dataclass
class PyArgument:
    """Python函数参数"""
    name: str
    type_expr: PyTypeExpr
    default_value: Optional[PyValueExpr] = None


@dataclass
class PyMethod:
    """Python方法"""
    name: str
    description_lines: List[str] = field(default_factory=list)
    return_type_expr: Optional[PyTypeExpr] = None
    arguments: List[PyArgument] = field(default_factory=list)
    vararg_position: Optional[int] = None
    is_static: bool = False
    is_overload: bool = False
    is_required: bool = False


@dataclass
class PyMember:
    """Python类成员（属性/字段）"""
    name: str
    type_expr: PyTypeExpr
    value_expr: Optional[PyValueExpr] = None
    inline_comment: Optional[str] = None


@dataclass
class SpecifiedPyMember:
    """直接指定字符串内容的Python成员"""
    specified_string: str
    inline_comment: Optional[str] = None


@dataclass
class PyClass:
    """Python类"""
    type: PyType
    description_lines: List[str] = field(default_factory=list)
    members: List[PyMember] = field(default_factory=list)
    class_attributes: List[PyMember] = field(default_factory=list)
    methods: List[PyMethod] = field(default_factory=list)
    
    # 类名别名映射
    CLASS_NAME_ALIAS: ClassVar[Dict[str, str]] = {"str":"String", "int":"Int", "float":"Float", "bool":"Bool"}
    # 需要忽略的类
    CLASS_IGNORED: ClassVar[Set[str]] = {"None"}
    # 需要忽略的方法
    METHOD_IGNORED: ClassVar[Set[str]] = {"__ne__", "__eq__"}
    
    # 所有类的索引
    ALL_CLASSES: ClassVar[Dict[PyType, List['PyClass']]] = {}
    
    def __post_init__(self):
        if self.type not in PyClass.ALL_CLASSES:
            PyClass.ALL_CLASSES[self.type] = []
        PyClass.ALL_CLASSES[self.type].append(self)


@dataclass
class PyFile:
    """Python文件"""
    name: str
    imports: List[str] = field(default_factory=list)
    description_lines: List[str] = field(default_factory=list)
    global_variables: List[Union[PyMember, SpecifiedPyMember]] = field(default_factory=list)
    global_functions: List[PyMethod] = field(default_factory=list)
    classes: List[PyClass] = field(default_factory=list)
    
    # 需要忽略的全局变量
    IGNORED_GLOBAL_VARIABLES: ClassVar[List[str]] = ["Script"] 