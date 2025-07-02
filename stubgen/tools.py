import types
from typing import Any, Union, get_origin, get_args, List, Dict, Set, Tuple
from dataclasses import fields
from enum import Enum
import traceback





DEBUG = True


def validate_types_on_init(cls):
    original_init = cls.__init__
    
    def __init__(self: Any, *args: Any, **kwargs: Any) -> None:
        original_init(self, *args, **kwargs)
        for field in fields(cls):
            # 特殊跳过_category字段，因为它可能包含不同模块路径的相同枚举
            if field.name == "_category":
                continue
                
            value = getattr(self, field.name)
            field_type = field.type
            
            try:
                check_type_match(value, field_type, field.name)
            except TypeError as e:
                if DEBUG:
                    traceback.print_exc()
                    raise TypeError(f"{e}, args: {args}, kwargs: {kwargs}, self: {self}")
                else:
                    raise
    
    cls.__init__ = __init__
    return cls


def check_type_match(value, expected_type, field_name=""):
    """递归检查值是否匹配预期类型"""
    
    # 如果 expected_type 是字符串，尝试用 eval 解析成类型表达式
    if isinstance(expected_type, str):
        try:
            # 尝试在全局和本地作用域中解析类型
            from .schema_py import PyType, PyTypeCategory, PyTypeExpr, PyClass, PyMethod, PyFile
            expected_type = eval(expected_type, globals(), locals())
        except Exception as e:
            raise TypeError(f"Failed to eval type annotation string '{expected_type}' for field '{field_name}': {e}")
    
    # 跳过Any类型的检查
    if expected_type == Any:
        return True
    
    # 特殊处理枚举值
    if isinstance(value, Enum):
        # 处理UnionType类型检查（|运算符）
        origin_type = get_origin(expected_type)
        if origin_type == Union or isinstance(origin_type, types.UnionType):
            type_args = get_args(expected_type)
            # 检查枚举类型是否包含在联合类型中
            for arg_type in type_args:
                # 通过类型名称比较而不是完整路径
                if isinstance(arg_type, type) and issubclass(arg_type, Enum) and arg_type.__name__ == type(value).__name__:
                    return True
                # 直接类型比较
                if arg_type == type(value):
                    return True
                # 处理None类型
                if arg_type is None and value is None:
                    return True
            # 枚举类型不在联合类型中
            raise TypeError(f"Expected '{field_name}' to be one of {type_args}, got {type(value)}, value: {value}")
        
        # 处理直接的枚举类型检查
        if isinstance(expected_type, type) and issubclass(expected_type, Enum):
            if isinstance(value, expected_type) or expected_type.__name__ == type(value).__name__:
                return True
            raise TypeError(f"Expected '{field_name}' to be {expected_type}, got {type(value)}, value: {value}")
    
    # 获取基础类型和泛型参数
    origin_type = get_origin(expected_type)
    type_args = get_args(expected_type)
    
    # 处理联合类型 (Union 或 | 操作符)
    if origin_type == types.UnionType:
        return check_union_type(value, type_args, field_name)
    
    # 基本检查类型
    check_type = origin_type if origin_type is not None else expected_type
    
    # 处理枚举类型 - 优先处理枚举，防止它被当作容器类型
    if isinstance(check_type, type) and issubclass(check_type, Enum):
        return check_enum_type(value, check_type, field_name)
    
    # 处理容器类型 - 只有真正的容器类型才进入这个分支
    # 注意: isinstance(Container, type)确保只有类型才会被考虑为容器
    if origin_type is not None and isinstance(check_type, type) and issubclass(check_type, (list, tuple, set, dict)):
        return check_container_type(value, check_type, type_args, field_name)
    
    # 处理普通类型
    if not isinstance(value, check_type):
        raise TypeError(f"Expected '{field_name}' to be {expected_type}, got {type(value)}, value: {value}")
    
    return True



def check_union_type(value, type_args, field_name):
    """检查值是否匹配联合类型中的任一类型"""
    # 特殊处理None值
    if value is None:
        for arg_type in type_args:
            if arg_type is None or arg_type is type(None):
                return True
        # None不匹配任何类型参数
        raise TypeError(f"Expected '{field_name}' to be one of {type_args}, got None")
    
    # 特殊处理枚举值
    if isinstance(value, Enum):
        # 查找匹配的枚举类型
        for arg_type in type_args:
            # 检查类型名称而不是完整路径
            if isinstance(arg_type, type) and issubclass(arg_type, Enum):
                if arg_type.__name__ == type(value).__name__ or isinstance(value, arg_type):
                    return True
            # 处理可能的无类型参数
            if arg_type == value.__class__ or arg_type == type(value):
                return True
    
    # 常规类型检查
    for arg_type in type_args:
        try:
            # 跳过None类型(已在上面处理)
            if arg_type is None or arg_type is type(None):
                continue
                
            check_type_match(value, arg_type, field_name)
            return True  # 匹配其中一个类型即可
        except TypeError:
            continue  # 继续检查下一个类型
    
    # 如果没有匹配到任何类型
    raise TypeError(f"Expected '{field_name}' to be one of {type_args}, got {type(value)}, value: {value}")


def check_enum_type(value, enum_type, field_name):
    """检查值是否为正确的枚举类型"""
    if isinstance(value, Enum):
        if not isinstance(value, enum_type):
            raise TypeError(f"Expected '{field_name}' to be {enum_type}, got {type(value)}, value: {value}")
    else:
        raise TypeError(f"Expected '{field_name}' to be an Enum of type {enum_type}, got {type(value)}, value: {value}")
    return True


def check_container_type(value, container_type, type_args, field_name):
    """检查容器类型及其内部元素"""
    # 检查容器本身的类型
    if not isinstance(value, container_type):
        raise TypeError(f"Expected '{field_name}' to be {container_type}, got {type(value)}, value: {value}")
    
    # 如果没有类型参数，不需要检查内部元素
    if not type_args:
        return True
    
    # 列表、集合等可迭代对象的检查
    if container_type in (list, tuple, set) or container_type == List or container_type == Tuple or container_type == Set:
        for i, item in enumerate(value):
            try:
                check_type_match(item, type_args[0], f"{field_name}[{i}]")
            except TypeError as e:
                raise TypeError(f"Item {i} in '{field_name}': {e}")
    
    # 字典类型的特殊处理
    elif container_type == dict or container_type == Dict:
        if len(type_args) == 2:
            for k, v in value.items():
                try:
                    check_type_match(k, type_args[0], f"{field_name}_key")
                except TypeError as e:
                    raise TypeError(f"Dict key in '{field_name}': {e}")
                
                try:
                    check_type_match(v, type_args[1], f"{field_name}[{k}]")
                except TypeError as e:
                    raise TypeError(f"Dict value for key '{k}' in '{field_name}': {e}")
    
    return True


class ValidatorResults():
    def __init__(self) -> None:
        self.results = []
    
    def append(self, result: bool) -> None:
        if DEBUG:
            if not result:
                raise ValueError(f"Validation failed")
        
        self.results.append(result)
        
    def result(self) -> bool:
        return all(self.results)


def build_dependency_graph(nodes: list, get_name_func, get_dependencies_func) -> dict[str, list[str]]:
    """
    通用的依赖图构建函数，用于不同类型的对象间依赖关系建模
    
    这个函数接受任意类型的节点列表，通过提供的访问器函数获取节点名称和依赖关系，
    构建一个表示依赖关系的有向图。生成的图可用于拓扑排序、循环依赖检测等。
    
    Args:
        nodes: 节点列表，可以是任何类型的对象
        get_name_func: 获取节点名称的函数，接收节点作为参数，返回字符串标识符
            例如: lambda node: node.name
        get_dependencies_func: 获取节点依赖的函数，接收节点作为参数，返回该节点依赖的
            其他节点名称列表（依赖节点的字符串标识符）
            例如: lambda node: [dep.name for dep in node.dependencies]
            
    Returns:
        依赖图，键为节点名称，值为该节点依赖的其他节点名称列表
        
    Examples:
        # 基于类的继承关系构建依赖图
        def get_class_name(cls):
            return cls.__name__
            
        def get_parent_classes(cls):
            return [base.__name__ for base in cls.__bases__ if base is not object]
            
        class_graph = build_dependency_graph([A, B, C], get_class_name, get_parent_classes)
        
        # 对于自定义对象的依赖关系
        def get_name(obj):
            return obj.name
            
        def get_deps(obj):
            return [ref.name for ref in obj.references]
            
        dependency_graph = build_dependency_graph(objects, get_name, get_deps)
    """
    dependency_graph = {}
    node_map = {get_name_func(node): node for node in nodes}
    
    # 构建依赖图
    for node in nodes:
        node_name = get_name_func(node)
        
        # 确保每个节点都在图中有一个条目
        if node_name not in dependency_graph:
            dependency_graph[node_name] = []
        
        # 获取该节点依赖的所有节点
        dependencies = get_dependencies_func(node)
        
        # 将依赖节点添加到依赖图
        for dep_name in dependencies:
            if dep_name != node_name and dep_name in node_map:
                if dep_name not in dependency_graph:
                    dependency_graph[dep_name] = []
                if dep_name not in dependency_graph[node_name]:
                    dependency_graph[node_name].append(dep_name)
                    
    return dependency_graph

def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    """
    对依赖图执行拓扑排序，确保依赖项在被依赖项之前
    
    该算法实现了对有向图的深度优先搜索拓扑排序，能够处理复杂的依赖网络，
    返回的结果保证：如果A依赖B，则B在结果列表中出现在A之前。
    算法也可以处理有环图，通过暂时标记节点来检测环，但不会抛出异常。
    
    Args:
        graph: 依赖图，键为节点名称，值为该节点依赖的节点名称列表
        
    Returns:
        排序后的节点名称列表，依赖在前，被依赖在后
        
    Examples:
        # 从依赖图获取正确的处理顺序
        graph = {
            'A': ['B', 'C'],  # A 依赖 B 和 C
            'B': ['D'],       # B 依赖 D
            'C': ['D'],       # C 依赖 D
            'D': []           # D 不依赖任何节点
        }
        order = topological_sort(graph)
        # 结果将是 ['D', 'B', 'C', 'A']，确保依赖在前
    """
    visited = set()
    temp_mark = set()
    ordered_nodes = []
    
    def visit(node):
        if node in temp_mark:
            # 检测到循环依赖，略过该节点以避免无限递归
            return
        if node not in visited:
            temp_mark.add(node)
            for dep in graph.get(node, []):
                visit(dep)
            temp_mark.remove(node)
            visited.add(node)
            ordered_nodes.append(node)
    
    # 为所有节点执行拓扑排序
    for node in graph:
        if node not in visited:
            visit(node)
    
    # 反转列表，使依赖在前，被依赖在后
    ordered_nodes.reverse()
    return ordered_nodes
