
from typing import TypeVar
from gdenums import *
from typings import *


class GDBuiltinClass[T: BuiltinBase]:
    def __init__(self, name: str): ...

class GDNativeClass[T: NativeBase]:
    def __init__(self, name: str): ...

class ExtendsHint[T: BuiltinBase | NativeBase]:
    @property
    def owner(self) -> T: ...

def Extends[T: NativeBase](cls: GDNativeClass[T]) -> type[ExtendsHint[T]]: ...

# e.g.
Resource = GDNativeClass[Resource]('Resource')

