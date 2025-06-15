
Object = object

class RefCounted(Object): pass

class Resource(RefCounted): pass

class Node(RefCounted): pass

class Extends[T: Object]:
    @property
    def owner(self) -> T: ...

def exposed(cls):
    cls.__exposed__ = True
    return cls

def export[T](type: type[T], default: T | None = None) -> T: ...
def export_range[T: int | float](min: T, max: T, step: T, default: T | None = None) -> T: ...

class MyClass(Extends[Node]):
    number = export(int)
    resource = export(Resource)
    my_node = export(Node)
    x_int = export_range(1, 10, 2)
    x_float = export_range(1.0, 10, 2)
