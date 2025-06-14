from dataclasses import dataclass
from godot_class import PropertyHint, PropertyUsageFlags # type: ignore

VariantType = int

@dataclass
class property:
    type: VariantType   # 来自模板参数（初始值，但后面可能会修改）
    name: str           # 变量的名字
    class_name: str
    hint: int           # 来自模板参数
    hint_string: str    # 参数列表用逗号拼接
    usage: int

def export(type: type) -> property:
    return property(hint=PropertyHint.PROPERTY_HINT_NONE)

def export_range(min: float, max: float, step: float, extra_hints: str) -> property:
    return property(hint=PropertyHint.PROPERTY_HINT_RANGE)