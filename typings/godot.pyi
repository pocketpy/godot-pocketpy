
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

def export[T](type: type[T]) -> T: ...
def export_range(min, max, step) -> float: ...

class MyClass(Extends[Node]):
    number = export(int)
    resource = export(Resource)
    my_node = export(Node)

    slider = export_range(-10, 20, 0.2)

