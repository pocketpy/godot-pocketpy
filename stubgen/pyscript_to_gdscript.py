from typing import TypeVar, Generic, ClassVar, List, Self, Any, Callable, Optional, Union, Dict, Tuple
from dataclasses import dataclass
from godot.enum import Enum, auto

# 类型变量定义
T = TypeVar('T')

# ============================================================================
# 上下文管理
# ============================================================================

@dataclass
class Context:
    """存储导出信息的上下文类"""
    exports: list[tuple[str, str, Any, str | None]] = None  # 属性名, 类型, 默认值, 分类
    extends: str | None = None  # 继承的Godot类
    categories: list[str] = None  # 分类列表
    export_calls: list[tuple[str, ...]] = None  # 导出调用记录
    ordered_properties: list[tuple[str, str | None]] = None  # (属性名, 分类)
    
    def __post_init__(self):
        if self.exports is None:
            self.exports = []
        if self.categories is None:
            self.categories = []
        if self.export_calls is None:
            self.export_calls = []
        if self.ordered_properties is None:
            self.ordered_properties = []
    
    def reset(self):
        """重置上下文状态"""
        self.exports.clear()
        self.extends = None
        self.categories.clear()
        self.export_calls.clear()
        self.ordered_properties.clear()
    
    def record_export_call(self, call_type: str, *args):
        """记录导出调用"""
        self.export_calls.append((call_type, *args))
    
    def add_category(self, category: str):
        """添加分类"""
        self.categories.append(category)
        self.record_export_call('export_category', category)
    
    def set_extends(self, gdt_cls: str):
        """设置继承类"""
        self.extends = gdt_cls

# 全局上下文实例
context = Context()

# ============================================================================
# 导出捕获
# ============================================================================

class ExportType(Enum):
    """导出类型枚举"""
    EXPORT = auto()
    RANGE = auto()
    ENUM = auto()
    FILE = auto()
    DIR = auto()
    GLOBAL_FILE = auto()
    GLOBAL_DIR = auto()
    MULTILINE = auto()
    COLOR = auto()
    NODE_PATH = auto()
    FLAGS = auto()
    FLAGS_2D_PHYSICS = auto()
    FLAGS_2D_RENDER = auto()
    FLAGS_2D_NAVIGATION = auto()
    FLAGS_3D_PHYSICS = auto()
    FLAGS_3D_RENDER = auto()
    FLAGS_3D_NAVIGATION = auto()
    STORAGE = auto()
    CUSTOM = auto()
    TOOL_BUTTON = auto()
    
    @classmethod
    def to_string(cls, export_type) -> str:
        """将枚举转换为字符串"""
        return export_type.name.lower()

@dataclass
class ExportCapture:
    """用于捕获export参数的类"""
    export_type: ExportType
    gdt_cls: str
    default: Any = None
    args: tuple = ()
    
    @property
    def export_type_str(self) -> str:
        """获取导出类型的字符串表示"""
        return ExportType.to_string(self.export_type)

# ============================================================================
# 继承机制
# ============================================================================

# class _ExtendedClass(type):
#     """用于标记继承自特定Godot类的元类"""
#     def __new__(mcs, name, bases, attrs):
#         cls = super().__new__(mcs, name, bases, attrs)
#         cls._parent_class_name = getattr(cls, '_parent_class_name', None)
#         return cls

def _Extends(gdt_cls: str) -> type:
    """创建一个带有_parent_class_name属性的类"""
    class_with_parent = type('ExtendedClass', (object,), {'_parent_class_name': gdt_cls})
    return class_with_parent

def Extends(gdt_cls: str) -> type:
    """标记一个类继承自特定的Godot类"""
    context.set_extends(gdt_cls)
    return _Extends(gdt_cls)

# ============================================================================
# 导出函数实现
# ============================================================================

def _export(cls: str, default: Any = None) -> str:
    """内部实现"""
    return f'importing from {cls}'

# 基础导出
def export(gdt_cls: str, default: Any = None) -> ExportCapture:
    """基本导出函数"""
    context.record_export_call('export', gdt_cls, default)
    return ExportCapture(ExportType.EXPORT, gdt_cls, default)

# 范围导出
def export_range(min_value: Union[int, float], max_value: Union[int, float], 
                step: Union[int, float] = 1, hint: str = "", or_greater: bool = False, 
                or_less: bool = False, default: Any = None) -> ExportCapture:
    """范围导出函数"""
    args = (min_value, max_value, step, hint, or_greater, or_less)
    context.record_export_call('export_range', *args, default)
    return ExportCapture(ExportType.RANGE, 'float' if isinstance(default, float) else 'int', default, args)

# 枚举导出
def export_enum(*options, default: Any = None) -> ExportCapture:
    """枚举导出函数"""
    context.record_export_call('export_enum', options, default)
    # 根据默认值确定类型
    gdt_cls = 'String' if isinstance(default, str) else 'int'
    return ExportCapture(ExportType.ENUM, gdt_cls, default, options)

# 文件路径导出
def export_file(filter: str = "", default: str = "") -> ExportCapture:
    """文件导出函数"""
    args = (filter,)
    context.record_export_call('export_file', *args, default)
    return ExportCapture(ExportType.FILE, 'String', default, args)

def export_dir(default: str = "") -> ExportCapture:
    """目录导出函数"""
    context.record_export_call('export_dir', default)
    return ExportCapture(ExportType.DIR, 'String', default)

def export_global_file(filter: str = "", default: str = "") -> ExportCapture:
    """全局文件导出函数"""
    args = (filter,)
    context.record_export_call('export_global_file', *args, default)
    return ExportCapture(ExportType.GLOBAL_FILE, 'String', default, args)

def export_global_dir(default: str = "") -> ExportCapture:
    """全局目录导出函数"""
    context.record_export_call('export_global_dir', default)
    return ExportCapture(ExportType.GLOBAL_DIR, 'String', default)

# 特殊文本导出
def export_multiline(default: str = "") -> ExportCapture:
    """多行文本导出函数"""
    context.record_export_call('export_multiline', default)
    return ExportCapture(ExportType.MULTILINE, 'String', default)

# 颜色导出
def export_color(show_alpha: bool = True, default: Any = None) -> ExportCapture:
    """颜色导出函数"""
    args = (show_alpha,)
    context.record_export_call('export_color', *args, default)
    return ExportCapture(ExportType.COLOR, 'Color', default, args)

# 节点路径导出
def export_node_path(node_type: str = "", default: str = "") -> ExportCapture:
    """节点路径导出函数"""
    args = (node_type,)
    context.record_export_call('export_node_path', *args, default)
    return ExportCapture(ExportType.NODE_PATH, 'NodePath', default, args)

# 标志位导出
def export_flags(*flags, default: int = 0) -> ExportCapture:
    """自定义标志位导出函数"""
    context.record_export_call('export_flags', flags, default)
    return ExportCapture(ExportType.FLAGS, 'int', default, flags)

def export_flags_2d_physics(default: int = 0) -> ExportCapture:
    """2D物理标志位导出函数"""
    context.record_export_call('export_flags_2d_physics', default)
    return ExportCapture(ExportType.FLAGS_2D_PHYSICS, 'int', default)

def export_flags_2d_render(default: int = 0) -> ExportCapture:
    """2D渲染标志位导出函数"""
    context.record_export_call('export_flags_2d_render', default)
    return ExportCapture(ExportType.FLAGS_2D_RENDER, 'int', default)

def export_flags_2d_navigation(default: int = 0) -> ExportCapture:
    """2D导航标志位导出函数"""
    context.record_export_call('export_flags_2d_navigation', default)
    return ExportCapture(ExportType.FLAGS_2D_NAVIGATION, 'int', default)

def export_flags_3d_physics(default: int = 0) -> ExportCapture:
    """3D物理标志位导出函数"""
    context.record_export_call('export_flags_3d_physics', default)
    return ExportCapture(ExportType.FLAGS_3D_PHYSICS, 'int', default)

def export_flags_3d_render(default: int = 0) -> ExportCapture:
    """3D渲染标志位导出函数"""
    context.record_export_call('export_flags_3d_render', default)
    return ExportCapture(ExportType.FLAGS_3D_RENDER, 'int', default)

def export_flags_3d_navigation(default: int = 0) -> ExportCapture:
    """3D导航标志位导出函数"""
    context.record_export_call('export_flags_3d_navigation', default)
    return ExportCapture(ExportType.FLAGS_3D_NAVIGATION, 'int', default)

# 高级导出
def export_storage(default: Any = None) -> ExportCapture:
    """存储导出函数，不在编辑器中显示但会被序列化"""
    context.record_export_call('export_storage', default)
    # 从默认值推断类型
    gdt_cls = type(default).__name__ if default is not None else 'Variant'
    return ExportCapture(ExportType.STORAGE, gdt_cls, default)

def export_custom(property_hint: int, hint_string: str = "", usage: int = 4102, default: Any = None) -> ExportCapture:
    """自定义属性提示导出函数"""
    args = (property_hint, hint_string, usage)
    context.record_export_call('export_custom', *args, default)
    # 从默认值推断类型
    gdt_cls = type(default).__name__ if default is not None else 'Variant'
    return ExportCapture(ExportType.CUSTOM, gdt_cls, default, args)

def export_tool_button(label: str = "", icon: str = "", callback: Callable = None) -> ExportCapture:
    """工具按钮导出函数"""
    args = (label, icon)
    context.record_export_call('export_tool_button', *args, callback)
    return ExportCapture(ExportType.TOOL_BUTTON, 'Callable', callback, args)

# 分类函数
def export_category(category: str) -> None:
    """设置后续属性的分类"""
    context.add_category(category)

# ============================================================================
# 类处理
# ============================================================================

def __class_begin__(ctx: Context) -> None:
    """开始处理类，重置上下文状态"""
    ctx.reset()

def __class_end__(ctx: Context, cls: type) -> type:
    """结束处理类，处理所有导出信息"""
    # 处理类的导出属性
    process_class_exports(ctx, cls)
    
    # 打印收集到的信息
    print_class_info(ctx, cls)
    
    return cls

def process_class_exports(ctx: Context, cls: type) -> None:
    """处理类的所有导出属性"""
    current_category: str | None = None
    exports_by_name: dict[str, ExportCapture] = {}
    
    # 收集所有导出的属性
    for attr_name, attr_value in cls.__dict__.items():
        if isinstance(attr_value, ExportCapture):
            exports_by_name[attr_name] = attr_value
            # 设置属性的实际值为占位符
            setattr(cls, attr_name, _export(attr_value.gdt_cls, attr_value.default))
    
    # 调试信息
    print(f"Found {len(exports_by_name)} exported properties")
    for name, export_capture in exports_by_name.items():
        print(f"  - {name}: {export_capture.export_type_str} ({export_capture.gdt_cls})")
    
    # 按照调用顺序重建属性列表
    for call_info in ctx.export_calls:
        call_type, *args = call_info
        
        if call_type == 'export_category':
            current_category = args[0]
            print(f"Processing category: {current_category}")
        else:
            # 找到对应的属性名
            print(f"Processing call type: {call_type} with args: {args}")
            match_export_property(ctx, exports_by_name, call_type, args, current_category)

def match_export_property(ctx: Context, exports_by_name: dict, call_type: str, args: list, current_category: str | None) -> None:
    """匹配导出属性与调用记录"""
    # 将call_type转换为export_type_str格式（去掉"export_"前缀）
    expected_export_type_str = call_type
    if call_type.startswith("export_"):
        expected_export_type_str = call_type[7:]  # 移除"export_"前缀
    
    for attr_name, export_capture in list(exports_by_name.items()):
        # 调试信息
        print(f"  Checking {attr_name}: {export_capture.export_type_str} vs {expected_export_type_str}")
        
        if export_capture.export_type_str == expected_export_type_str:
            # 检查参数是否匹配
            if match_export_args(call_type, export_capture, args):
                # 添加到导出列表
                ctx.exports.append((attr_name, export_capture.gdt_cls, export_capture.default, current_category))
                ctx.ordered_properties.append((attr_name, current_category))
                # 从待处理列表中移除
                del exports_by_name[attr_name]
                print(f"  ✓ Matched {attr_name} to {call_type}")
                break
            else:
                print(f"  ✗ Args didn't match for {attr_name}")

def match_export_args(call_type: str, export_capture: ExportCapture, args: list) -> bool:
    """检查导出参数是否匹配调用记录"""
    # 调试信息
    print(f"    Matching args for {call_type}: {export_capture.default} vs {args[-1] if args else None}")
    
    if call_type == 'export':
        return export_capture.gdt_cls == args[0] and export_capture.default == args[1]
    else:
        # 对于大多数导出类型，默认值应该是最后一个参数
        # 由于装饰器的工作方式，我们只需检查默认值是否匹配
        return args and export_capture.default == args[-1]

def print_class_info(ctx: Context, cls: type) -> None:
    """打印类的导出信息"""
    print("\n=== Class Information ===")
    print(f"Class: {cls.__name__}")
    print(f"Extends: {ctx.extends}")
    print("Exported properties:")
    for prop_name, prop_type, default_value, category in ctx.exports:
        print(f"  - {prop_name}: {prop_type} = {default_value} (Category: {category})")

# ============================================================================
# 示例使用
# ============================================================================


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

# 开始处理示例类
__class_begin__(context)

class A(Extends('Node')):
    export_category('Basic Properties')
    x = export('int', 1)
    y = export('float', 2.5)
    z = export('String', "Hello")
    
    export_category('Range Properties')
    health = export_range(0, 100, 1, "or_greater", False, False, 100)
    speed = export_range(0.0, 10.0, 0.1, default=5.0)
    
    export_category('Enum Properties')
    character_class = export_enum("Warrior", "Magician", "Thief", default=0)
    character_name = export_enum("Rebecca", "Mary", "Leah", default="Rebecca")
    
    export_category('File Properties')
    config_file = export_file("*.json", "config.json")
    save_dir = export_dir("saves")
    global_config = export_global_file("*.cfg", "/etc/app/config.cfg")
    global_data_dir = export_global_dir("/var/data")
    
    export_category('Other Properties')
    description = export_multiline("A multi-line\ndescription")
    player_color = export_color(True, None)  # Default to null Color
    target_node = export_node_path("Enemy", "../Enemy")
    collision_layers = export_flags("Layer1", "Layer2", "Layer3", default=1)  # Layer1 enabled
    physics_layers = export_flags_2d_physics(3)  # Layers 1 and 2 enabled
    
    export_category('Advanced Properties')
    internal_data = export_storage({"hidden": "value"})
    altitude = export_custom(0, "altitude:m", 4102, Vector3(0, 0, 0))
    
    @staticmethod
    def hello_action():
        print("Hello world!")
    
    hello_button = export_tool_button("Hello", "Callable", hello_action)

# 结束处理示例类
__class_end__(context, A)


