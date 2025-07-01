extends Node

class_name NewScript

@export var x: int = 10
@export var y: Node
@export_range(1.2, 10.2, 0.1) var z = 5.0
@export var w: String = 'ab'

func _ready() -> void:
	var c = test
	print(c.call(1, 2))

func test(a: int, b: float):
	return a + b
