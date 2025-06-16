from typing import Any

def exposed(cls):
    """
    Decorator to mark a class as exposed to the Godot Engine.
    """

class Object: ...

class Node: ...

class Extends[T: Object]:
    @property
    def owner(self) -> T: ...