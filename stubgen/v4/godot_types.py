from enum import Enum
import re
from typing import Dict, List, Optional, Set, Tuple, Union, Any

from .schema_py import PyType, PyTypeExpr, PyValueExpr, PyMethod, PyClass
from ..schema_gdt import GodotInOne


class GodotTypeCategory(Enum):
    """Godot类型分类"""
    CAN_TRANSFER_TO_PY_BUILTIN = "CAN_TRANSFER_TO_PY_BUILTIN"  # 可以直接映射到Python内置类型
    GODOT_NATIVE = "GODOT_NATIVE"                # Godot原生类型
    ENUM = "ENUM"                               # 枚举类型
    SINGLETON_GODOT_NATIVE = "SINGLETON_GODOT_NATIVE"  # 单例类型
    IGNORE = "IGNORE"                           # 忽略的类型


class GodotValueCategory(Enum):
    """Godot值分类"""
    UNKNOWN = 0        # 未知类型
    OTHER_TYPE = 1     # 其他类型
    NULL = 2           # 空值
    ENUM_CONST = 3     # 枚举常量
    INT = 4            # 整数
    FLOAT = 5          # 浮点数
    STR = 6            # 字符串
    BOOL = 7           # 布尔值
    STRING_NAME = 8    # 字符串名称


# Godot操作符映射到Python方法名
GODOT_OPERATORS_TABLE: Dict[str, str] = {
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

# 不支持的操作符
NOT_SUPPORTED_OPERATORS: Dict[str, str] = {
    'unary+': '__pos__',
    'not': '__invert__',
    'and': '__and__',
    'or': '__or__',
    'xor': '__xor__',
}

# 内置类型映射表
COMPATIBLE_TYPES_MAP: Dict[str, str] = {"Nil": 'None', "int": 'int', "float": 'float', "bool": 'bool', "String": 'str'}


class GodotTypeRegistry:
    """Godot类型注册表"""
    # 类型分类集合
    COMPATIBLE_TYPES: Set[PyType] = set()       # 可直接映射到Python内置类型的类型
    GODOT_NATIVE_TYPES: Set[PyType] = set()     # Godot原生类型
    ENUM_TYPES: Set[PyType] = set()             # 枚举类型
    SINGLETON_GODOT_NATIVE_TYPES: Set[PyType] = set()  # 单例类型
    IGNORE_TYPES: Set[PyType] = set()           # 忽略的类型
    SUPPORT_GENERIC_TYPES: Set[PyType] = set()  # 支持泛型的类型
    
    # 继承关系缓存
    _SUBCLASSES_CACHE: Dict[str, Set[PyType]] = {}
    _SUPERCLASSES_CACHE: Dict[str, Set[PyType]] = {}
    
    @classmethod
    def register_type(cls, pytype: PyType, category: GodotTypeCategory) -> None:
        """注册类型到指定分类"""
        if category == GodotTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN:
            cls.COMPATIBLE_TYPES.add(pytype)
        elif category == GodotTypeCategory.GODOT_NATIVE:
            cls.GODOT_NATIVE_TYPES.add(pytype)
        elif category == GodotTypeCategory.ENUM:
            cls.ENUM_TYPES.add(pytype)
        elif category == GodotTypeCategory.SINGLETON_GODOT_NATIVE:
            cls.SINGLETON_GODOT_NATIVE_TYPES.add(pytype)
        elif category == GodotTypeCategory.IGNORE:
            cls.IGNORE_TYPES.add(pytype)
        else:
            raise ValueError(f"无效的类型分类: {category}")
    
    @classmethod
    def get_category(cls, pytype: PyType) -> GodotTypeCategory:
        """获取类型的分类"""
        if pytype in cls.COMPATIBLE_TYPES:
            return GodotTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN
        if pytype in cls.SINGLETON_GODOT_NATIVE_TYPES:  # 优先级更高
            return GodotTypeCategory.SINGLETON_GODOT_NATIVE
        if pytype in cls.ENUM_TYPES:
            return GodotTypeCategory.ENUM
        if pytype in cls.GODOT_NATIVE_TYPES:
            return GodotTypeCategory.GODOT_NATIVE
        if pytype in cls.IGNORE_TYPES:
            return GodotTypeCategory.IGNORE
        raise ValueError(f"类型 {pytype.name} 未在任何分类中找到")
    
    @classmethod
    def is_support_generic(cls, pytype: PyType) -> bool:
        """检查类型是否支持泛型"""
        return pytype in cls.SUPPORT_GENERIC_TYPES
    
    @classmethod
    def get_superclasses(cls, base_type: PyType, include_basetype: bool=False) -> Set[PyType]:
        """获取指定类型的所有父类"""
        if base_type.name in cls._SUPERCLASSES_CACHE:
            return cls._SUPERCLASSES_CACHE[base_type.name]
        
        superclasses = set([] if not include_basetype else [base_type])
        
        if base_type.inherit:
            superclasses.add(base_type.inherit)
            superclasses.update(cls.get_superclasses(base_type.inherit, include_basetype=include_basetype))
        
        cls._SUPERCLASSES_CACHE[base_type.name] = superclasses
        
        return superclasses
    
    @classmethod
    def get_subclasses(cls, base_type: PyType, include_basetype: bool=False) -> Set[PyType]:
        """获取指定类型的所有子类"""
        if base_type.name in cls._SUBCLASSES_CACHE:
            return cls._SUBCLASSES_CACHE[base_type.name]
        
        subclasses = set([] if not include_basetype else [base_type])
        
        # 直接子类
        direct_subclasses = [t for t in PyType.ALL_TYPES.values() if t.inherit == base_type]
        
        # 递归查找所有子类
        for subclass in direct_subclasses:
            subclasses.add(subclass)
            # 递归获取子类的子类
            subclasses.update(cls.get_subclasses(subclass, include_basetype=include_basetype))
        
        # 将结果存入缓存
        cls._SUBCLASSES_CACHE[base_type.name] = subclasses
        
        return subclasses


class GodotTypeParser:
    """Godot类型解析器"""
    
    @classmethod
    def parse_type_name(cls, name: str) -> str:
        """解析类型名称"""
        result = cls.try_parse_type_name(name, raise_error=True)
        if result is None:
            raise ValueError(f"找不到类型: {name}")
        return result
    
    @classmethod
    def try_parse_type_name(cls, name: str, raise_error: bool = True) -> Optional[str]:
        """尝试解析类型名称"""
        # 内置类型
        if name in COMPATIBLE_TYPES_MAP:
            return COMPATIBLE_TYPES_MAP[name]
        
        # 枚举类型
        if name.startswith('enum::'):
            return name.replace('enum::', '').replace('.', "__")
        
        # 也是枚举类型，包含"."但是不包含"::"的类型
        if '.' in name and '::' not in name:
            return name.replace('.', "__")
        
        # 位域类型
        if name.startswith('bitfield::'):
            return name.replace('bitfield::', '').replace('.', "__")
        
        # typedarray
        if name.startswith('typedarray::') or name == 'typedarray':
            return "Array"
        
        # 正常类型(名字合法的内置类型和原生类型)
        if bool(re.fullmatch(r'[A-Za-z0-9_]+', name)):
            return name
        
        # 引用类型的指针(intptr)
        # "xxx*" / "xxx**"
        if bool(re.fullmatch(r'[A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        # "const xxx*" / "const xxx**"
        if bool(re.fullmatch(r'const [A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        # "xxx,xxx*" / "xxx,xxx**"
        if bool(re.fullmatch(r'[A-Za-z0-9_]+\.[A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        # const xxx.xxx* / const xxx.xxx**
        if bool(re.fullmatch(r'const [A-Za-z0-9_]+\.[A-Za-z0-9_]*\s?\*\*?', name)):
            return 'intptr'
        
        if raise_error:
            raise ValueError(f"未知类型: {name}")
        return None
    
    @classmethod
    def parse_signal_type(cls, expr: str) -> Tuple[str, List[Tuple[str, str]]]:
        """解析信号类型表达式
        
        Signal(Callable((arg1:type1|arg2:type2...), return_type))
        """
        # 检查是否是符合 Signal(Callable((args), return_type)) 格式
        match = re.match(r'Signal\(Callable\(\((.*?)\), ([A-Za-z0-9_]+)\)\)', expr)
        if not match:
            raise ValueError(f"无效的信号类型格式: {expr}")
        
        # 处理参数部分
        args_part = match.group(1).strip()
        args_matched = []
        if args_part:  # 只有当参数部分非空时才分割
            args_matched = [arg.strip() for arg in args_part.split('|')]
        return_type_matched = match.group(2).strip()
        
        # 解析参数列表
        args = []
        for arg in args_matched:
            if not re.match(r'[A-Za-z0-9_]+:[A-Za-z0-9_]+', arg):
                raise ValueError(f"无效的信号类型格式: {expr}，解析参数时出错: {arg}")
            
            arg_name, arg_type = arg.split(':')
            args.append((arg_name, arg_type))
        
        return return_type_matched, args
    
    @classmethod
    def parse_generic_type(cls, expr: str) -> Tuple[str, Optional[str]]:
        """解析泛型类型表达式"""
        # 目前只有typedarray支持泛型
        if expr.startswith('typedarray::'):
            # typedarray::21/9:xxx  --> Array[xxx]
            if bool(re.fullmatch(r'typedarray::[0-9]*/[0-9]*:[A-Za-z0-9_]+', expr)):
                match = re.search(r'[0-9]*/[0-9]*:', expr)
                inner_type_expr = expr.replace('typedarray::', '')
                if match:
                    inner_type_expr = inner_type_expr.replace(match.group(), '')
                else:
                    raise ValueError(f"无效的typedarray表达式: {expr}")
                return "Array", inner_type_expr
            
            # typedarray::21/9:  --> Array
            if bool(re.fullmatch(r'typedarray::[0-9]*/[0-9]*:', expr)):
                return "Array", None
            
            # typedarray::xxx  --> Array[xxx]
            inner_type_expr = expr.replace('typedarray::', '')
            return "Array", inner_type_expr
        else:
            return expr, None
    
    @classmethod
    def parse_union_type(cls, expr: str) -> List[Tuple[str, Optional[str]]]:
        """解析联合类型表达式"""
        union_exprs = [sub_expr.strip() for sub_expr in expr.split(",")]
        
        if len(union_exprs) == 1:
            return [cls.parse_generic_type(expr)]
        
        # 处理特殊的排除模式： "aaa,-bbb,-ccc"
        is_exclude_pattern = True
        for i, expr in enumerate(union_exprs):
            if i == 0 and expr.startswith('-'):
                is_exclude_pattern = False
                break
            if i > 0 and not expr.startswith('-'):
                is_exclude_pattern = False
                break
        
        if is_exclude_pattern:
            # 这里只是返回解析结果，不处理实际排除逻辑
            result = []
            base_type = union_exprs[0]
            exclude_types = [expr.lstrip('-') for expr in union_exprs[1:]]
            result.append((base_type, None))
            for exclude_type in exclude_types:
                result.append((f"-{exclude_type}", None))
            return result
        else:
            # 普通的联合类型
            result = []
            for union_expr in union_exprs:
                result.append(cls.parse_generic_type(union_expr))
            return result


def map_godot_value_category(value_expr: str, type_expr: PyTypeExpr, type_registry: GodotTypeRegistry) -> GodotValueCategory:
    """映射Godot值类型到分类"""
    if value_expr == 'null':
        return GodotValueCategory.NULL
    
    # TODO: 实现更多映射逻辑
    
    return GodotValueCategory.UNKNOWN


def try_parse_operator_name(operator_name: str) -> Optional[str]:
    """尝试解析操作符名称为Python方法名"""
    if operator_name in GODOT_OPERATORS_TABLE:
        return GODOT_OPERATORS_TABLE[operator_name]
    
    if operator_name in NOT_SUPPORTED_OPERATORS:
        return None  # 不支持的操作符
    
    # 正常方法名
    if bool(re.fullmatch(r'[A-Za-z0-9_]+', operator_name)):
        return operator_name
    
    # 无法识别的操作符
    return None 