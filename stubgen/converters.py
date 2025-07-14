from dataclasses import dataclass
from keyword import iskeyword
import re
import pandas as pd

from typing import Any


# =====tools=====
def is_valid_type_name(s: str) -> bool:
    """
    ✅ MyType（单个类型名）
    ✅ MyType.SubType（点分隔）
    ✅ my_type.sub_type123（带数字和下划线）
    ✅ a.b.c.d（多层嵌套）
    ❌ .Type（以点开头）
    ❌ Type.（以点结尾）
    ❌ Type..SubType（连续两个点）
    ❌ 123Type（数字开头）
    ❌ MyType.123Sub（点后数字开头）
    """
    return bool(re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*$", s))


# =====业务=====
def convert_keyword_name(s: str) -> str:
    if iskeyword(s):
        return s + "_"
    else:
        return s


BUILTIN_CLASS_NAME_MAPPER: dict[str, str] = {
    "str": "String",
    "int": "Int",
    "float": "Float",
    "bool": "Bool",
}
GENERIC_CLASS_MAP: dict[str, str] = {
    "Signal": "Signal[T]",
    "Callable": "Callable[T, R]",
    "Array": "Array[T]",
}


def convert_class_name(name: str) -> str:
    assert name is not None
    assert name != ""
    # 内置类型
    result = None
    if name in BUILTIN_CLASS_NAME_MAPPER:
        result = BUILTIN_CLASS_NAME_MAPPER[name]
    else:
        result = name

    # 泛型类型
    if name in GENERIC_CLASS_MAP:
        result = GENERIC_CLASS_MAP[name]

    if not result or not is_valid_type_name(name):
        raise ValueError(f"Invalid type name: {name}")
    return result


COMPATIBLE_TYPES_MAP: dict[str, str] = {
    "Nil": "None",
    "int": "int",
    "float": "float",
    "bool": "bool",
    "String": "str",
}


def convert_type_name(name: str) -> str:

    # 复合类型
    if "," in name:
        return "typing.Any"  # TODO: 第三轮

    # 内置类型
    result = None
    if name in COMPATIBLE_TYPES_MAP:
        result = COMPATIBLE_TYPES_MAP[name]

    # 枚举类型
    elif name.startswith("enum::"):
        enum_name = name.replace("enum::", "")
        class_enum_results = find_records(
            CLASS_ENUM_DATA, {"orign_enum_name": enum_name}
        )
        if len(class_enum_results) > 0:
            result = (
                class_enum_results.iloc[0].loc["cls_enum_name"]
                + "."
                + class_enum_results.iloc[0].loc["enum_name"]
            )
        else:
            global_enum_results = find_records(
                GLOBAL_ENUMS_DATA, {"orign_enum_name": enum_name}
            )
            if len(global_enum_results) > 0:
                result = global_enum_results.iloc[0].loc["converted_enum_name"]
            else:
                raise Exception(f"无法找到枚举类型: {name}")

    # 也是枚举类型, 包含"."但是不包含"::"的类型
    elif "." in name and "::" not in name:
        enum_name = name
        class_enum_results = find_records(
            CLASS_ENUM_DATA, {"orign_enum_name": enum_name}
        )
        if len(class_enum_results) > 0:
            result = (
                class_enum_results.iloc[0].loc["cls_enum_name"]
                + "."
                + class_enum_results.iloc[0].loc["enum_name"]
            )
        else:
            global_enum_results = find_records(
                GLOBAL_ENUMS_DATA, {"orign_enum_name": enum_name}
            )
            if len(global_enum_results) > 0:
                result = global_enum_results.iloc[0].loc["converted_enum_name"]
            else:
                raise Exception(f"无法找到枚举类型: {name}")

    # 位域类型
    elif name.startswith("bitfield::"):
        result = "int"

    # typedarray
    elif name.startswith("typedarray::") or name == "typedarray":
        result = "Array"

    # 正常类型(名字合法的内置类型和原生类型)
    elif bool(re.fullmatch(r"[A-Za-z0-9_]+", name)):
        result = name

    # 引用类型的指针(intptr)
    # "xxx*" / "xxx**"
    elif bool(re.fullmatch(r"[A-Za-z0-9_]*\s?\*\*?", name)):
        result = "intptr"
    # "const xxx*" / "const xxx**"
    elif bool(re.fullmatch(r"const [A-Za-z0-9_]*\s?\*\*?", name)):
        result = "intptr"
    # "xxx,xxx*" / "xxx,xxx**"
    elif bool(re.fullmatch(r"[A-Za-z0-9_]+\.[A-Za-z0-9_]*\s?\*\*?", name)):
        result = "intptr"
    # const xxx.xxx* / const xxx.xxx**
    elif bool(re.fullmatch(r"const [A-Za-z0-9_]+\.[A-Za-z0-9_]*\s?\*\*?", name)):
        result = "intptr"

    if not result or not is_valid_type_name(result):
        raise ValueError(f"Unknown type: {name}")
    return result


BUILTIN_TYPES: set[str] = set()
NATIVE_TYPES: set[str] = set()


def get_ALL_TYPES() -> set[str]:
    return BUILTIN_TYPES | NATIVE_TYPES


CLASS_ENUM_DATA = pd.DataFrame(
    {
        "cls_name": [],
        "orign_enum_name": [],
        "cls_enum_name": [],
        "enum_name": [],
        "enum_constant_name": [],
        "constant_value": [],
    }
)


GLOBAL_ENUMS_DATA = pd.DataFrame(
    {
        "orign_enum_name": [],
        "converted_enum_name": [],
        "enum_constant_name": [],
        "constant_value": [],
    }
)


def find_records(df, condition_dict) -> pd.DataFrame:
    """
    根据字典条件查找匹配的记录
    :param df: 目标DataFrame
    :param condition_dict: 查询条件字典，如 {"cls_name": "MyClass", "enum_name": "Color"}
    :return: 匹配的DataFrame子集
    """
    if not condition_dict:
        return df.copy()

    # 构建多条件布尔索引
    condition = pd.Series(True, index=df.index)
    for col, val in condition_dict.items():
        if col in df.columns:
            condition &= df[col] == val
    return df[condition].copy()


def update_records(df, condition_dict, update_dict):
    """
    更新匹配条件的记录
    :param df: 目标DataFrame (CLASS_ENUM_DATA)
    :param condition_dict: 筛选条件字典
    :param update_dict: 更新字段字典，如 {"constant_value": 100, "enum_name": "NewName"}
    """
    if not condition_dict or not update_dict:
        return

    # 定位目标行
    condition = pd.Series(True, index=df.index)
    for col, val in condition_dict.items():
        if col in df.columns:
            condition &= df[col] == val

    # 批量更新字段 [1,9,11](@ref)
    for col, new_val in update_dict.items():
        if col in df.columns:
            df.loc[condition, col] = new_val


def append_records(
    df: pd.DataFrame, new_records: list[dict[str, Any]] | dict[str, Any]
) -> pd.DataFrame:
    """
    追加新记录到DataFrame
    :param df: 目标DataFrame
    :param new_records: 新记录列表，每个元素为字段字典
    :return: 追加后的DataFrame（原DataFrame会被修改）
    """
    required_columns = df.columns
    new_records = new_records if isinstance(new_records, list) else [new_records]
    for record in new_records:
        # 验证记录完整性
        if not all(col in record for col in required_columns):
            missing = set(required_columns) - set(record.keys())
            raise ValueError(f"Missing required columns: {missing}")

        # 追加记录
        df.loc[len(df)] = [record[col] for col in required_columns]

    return df


OPERATORS_TABLE = {
    "<": "__lt__",
    "<=": "__le__",
    ">": "__gt__",
    ">=": "__ge__",
    "+": "__add__",
    "-": "__sub__",
    "*": "__mul__",
    "/": "__truediv__",
    "%": "__mod__",
    "**": "__pow__",
    "<<": "__lshift__",
    ">>": "__rshift__",
    "&": "__and__",
    "|": "__or__",
    "^": "__xor__",
    "in": "__contains__",
    "unary-": "__neg__",
    "~": "__invert__",
}

NOT_SUPPORTED_OPERATORS = {
    "unary+": "__pos__",
    "not": "__invert__",
    "and": "__and__",
    "or": "__or__",
    "xor": "__xor__",
    "==": "__eq__",
    "!=": "__ne__",
}

BUILTIN_CLASSES_SUPPORTED_OPERATOR_DATA = pd.DataFrame(
    {
        "orign_cls_name": [],  # 原始的类名
        "cls_name": [],  # 转换后的类名
        "orign_op_name": [],  # 原始的运算符名称
        "op_name": [],  # 转换后的运算符名称
    }
)


def is_supported_operator(op: str) -> bool:
    return op in OPERATORS_TABLE


def is_overload_operator(cls_name, op_name: str) -> bool:
    return (
        len(
            find_records(
                BUILTIN_CLASSES_SUPPORTED_OPERATOR_DATA,
                {"cls_name": cls_name, "op_name": op_name},
            )
        )
        > 1
    )


def convert_operator_to_method_name(op: str) -> str:
    if op not in OPERATORS_TABLE:
        raise ValueError(f"不支持的操作符: {op}")
    return OPERATORS_TABLE.get(op, op)


