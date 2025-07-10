import re
from typing import Dict, List, Optional, Set, Tuple, Any

from .schema_py import PyType, PyTypeExpr, PyValueExpr
from .godot_types import (
    GodotTypeCategory, GodotTypeRegistry, GodotTypeParser, COMPATIBLE_TYPES_MAP
)
from ..schema_gdt import GodotInOne
from ..tools import ValidatorResults, DEBUG


class TypeManager:
    """
    类型管理器 - 负责创建和管理类型
    """
    
    @classmethod
    def get_type(cls, name: str) -> PyType:
        """
        根据名称获取类型
        
        Args:
            name: 类型名称
            
        Returns:
            PyType: 对应的类型对象
            
        Raises:
            ValueError: 如果类型不存在
        """
        result = cls._get_type(name, raise_error=True)
        if result is None:
            raise ValueError(f"找不到类型: {name}")
        return result
    
    @classmethod
    def try_get_type(cls, name: str) -> Optional[PyType]:
        """
        尝试获取类型，如果不存在则返回None
        
        Args:
            name: 类型名称
            
        Returns:
            PyType或None: 对应的类型对象，如果不存在则为None
        """
        return cls._get_type(name, raise_error=False)
    
    @classmethod
    def _get_type(cls, name: str, raise_error: bool = True) -> Optional[PyType]:
        """
        内部方法：获取类型
        
        Args:
            name: 类型名称
            raise_error: 是否在类型不存在时抛出异常
            
        Returns:
            PyType或None: 对应的类型对象，如果不存在且raise_error为False则为None
            
        Raises:
            ValueError: 如果类型不存在且raise_error为True
        """
        name = GodotTypeParser.parse_type_name(name)
        if name not in PyType.ALL_TYPES:
            if raise_error:
                # 按首字母分组打印类型名
                type_names = sorted(PyType.ALL_TYPES.keys())
                grouped_types: Dict[str, List[str]] = {}
                for type_name in type_names:
                    first_letter = type_name[0].upper()
                    if first_letter not in grouped_types:
                        grouped_types[first_letter] = []
                    grouped_types[first_letter].append(type_name)
                
                error_msg = f"找不到类型: {name}\n\tALL_TYPES:\n"
                for letter in sorted(grouped_types.keys()):
                    error_msg += f"\t{letter}: {', '.join(grouped_types[letter])}\n"
                
                raise ValueError(error_msg.rstrip())
            return None
        return PyType.ALL_TYPES[name]
    
    @classmethod
    def add_type(cls, name: str, category: GodotTypeCategory) -> None:
        """
        添加类型
        
        Args:
            name: 类型名称
            category: 类型分类
            
        Raises:
            ValueError: 如果类型无效
        """
        name = GodotTypeParser.parse_type_name(name)
        new_pytype = PyType(name=name)
        if not cls.validate_type(new_pytype):
            raise ValueError(f"无效的类型: {name}")
        
        PyType.ALL_TYPES[name] = new_pytype
        
        # 强制识别并添加内置类型
        if name in COMPATIBLE_TYPES_MAP or name in COMPATIBLE_TYPES_MAP.values():
            GodotTypeRegistry.register_type(new_pytype, GodotTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN)
        else:
            GodotTypeRegistry.register_type(new_pytype, category)
    
    @classmethod
    def get_superclasses(cls, base_type: PyType, include_basetype: bool=False) -> Set[PyType]:
        """
        获取类型的所有父类
        
        Args:
            base_type: 基础类型
            include_basetype: 是否包含基础类型自身
            
        Returns:
            Set[PyType]: 父类集合
        """
        return GodotTypeRegistry.get_superclasses(base_type, include_basetype)
    
    @classmethod
    def get_subclasses(cls, base_type: PyType, include_basetype: bool=False) -> Set[PyType]:
        """
        获取类型的所有子类
        
        Args:
            base_type: 基础类型
            include_basetype: 是否包含基础类型自身
            
        Returns:
            Set[PyType]: 子类集合
        """
        return GodotTypeRegistry.get_subclasses(base_type, include_basetype)
    
    @classmethod
    def build_type_sets(cls, gdt_all_in_one: GodotInOne) -> None:
        """
        从Godot类型定义构建类型集合
        
        Args:
            gdt_all_in_one: Godot类型定义
        """
        # 支持泛型的类型
        for name in ['Array']:
            PyType.ALL_TYPES[name] = PyType(name=name)
            GodotTypeRegistry.SUPPORT_GENERIC_TYPES.add(cls.get_type(name))
        
        # Variant
        cls.add_type('Variant', GodotTypeCategory.CAN_TRANSFER_TO_PY_BUILTIN)
        
        # intptr
        cls.add_type('intptr', GodotTypeCategory.IGNORE)
        
        # Enum
        cls.add_type('Enum', GodotTypeCategory.IGNORE)
        
        # 单例类型
        for singleton_data in gdt_all_in_one.singletons:
            cls.add_type(singleton_data.name, GodotTypeCategory.SINGLETON_GODOT_NATIVE)
        
        # 内置类型
        for builtin_class in gdt_all_in_one.builtin_classes:
            cls.add_type(builtin_class.name, GodotTypeCategory.GODOT_NATIVE)
        
        # 枚举和原生类型
        for cls_data in gdt_all_in_one.classes:
            cls.add_type(cls_data.name, GodotTypeCategory.GODOT_NATIVE)
            
            if cls_data.enums:
                for enum_data in cls_data.enums:
                    name = cls_data.name + '__' + enum_data.name
                    cls.add_type(name, GodotTypeCategory.ENUM)
                    cls.get_type(name).inherit = cls.get_type("Enum")
        
        for builtin_cls_data in gdt_all_in_one.builtin_classes:
            if builtin_cls_data.enums:
                for enum_data in builtin_cls_data.enums:
                    name = builtin_cls_data.name + '__' + enum_data.name
                    cls.add_type(name, GodotTypeCategory.ENUM)
                    cls.get_type(name).inherit = cls.get_type("Enum")
        
        for enum_data in gdt_all_in_one.global_enums:
            cls.add_type(enum_data.name, GodotTypeCategory.ENUM)
            cls.get_type(enum_data.name).inherit = cls.get_type("Enum")
        
        # 设置继承关系
        for cls_data in gdt_all_in_one.classes:
            if cls_data.inherits:
                cls.get_type(cls_data.name).inherit = cls.get_type(cls_data.inherits)
            else:
                # Object类型特殊处理
                if cls_data.name == "Object":
                    cls.get_type(cls_data.name).inherit = cls.get_type("Variant")
                else:
                    raise ValueError(f"原生类 '{cls_data.name}' 没有继承关系")
        
        # 内置类的类型继承自Variant
        for builtin_cls_data in gdt_all_in_one.builtin_classes:
            cls.get_type(builtin_cls_data.name).inherit = cls.get_type("Variant")
    
    @staticmethod
    def validate_type(pytype: PyType) -> bool:
        """
        验证类型是否有效
        
        Args:
            pytype: 要验证的类型
            
        Returns:
            bool: 是否有效
        """
        results = ValidatorResults()
        results.append(bool(re.fullmatch(r'[A-Za-z0-9_]+', pytype.name)))
        return results.result()


class TypeExprFactory:
    """
    类型表达式工厂 - 用于创建和管理类型表达式
    """
    
    @classmethod
    def create_type_expr(cls, type_str: str) -> PyTypeExpr:
        """
        创建类型表达式
        
        Args:
            type_str: 类型表达式字符串
            
        Returns:
            PyTypeExpr: 类型表达式对象
        """
        if type_str in PyTypeExpr.ALL_TYPE_EXPRS:
            return PyTypeExpr.ALL_TYPE_EXPRS[type_str]
        
        type_expr = PyTypeExpr(expr_str=type_str)
        PyTypeExpr.ALL_TYPE_EXPRS[type_str] = type_expr
        return type_expr
    
    @classmethod
    def create_value_expr(cls, value_str: str, type_expr: PyTypeExpr) -> PyValueExpr:
        """
        创建值表达式
        
        Args:
            value_str: 值表达式字符串
            type_expr: 类型表达式
            
        Returns:
            PyValueExpr: 值表达式对象
        """
        return PyValueExpr(value_expr=value_str, type_expr=type_expr)
    
    @classmethod
    def get_type_expr_str(cls, type_expr: PyTypeExpr) -> str:
        """
        获取类型表达式的字符串表示
        
        Args:
            type_expr: 类型表达式
            
        Returns:
            str: 类型表达式字符串
        """
        return type_expr.expr_str 