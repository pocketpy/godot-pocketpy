extends Node

class_name NewScript

@export var x: int = 10
@export var y: Node
@export_range(1.2, 10.2, 0.1) var z = 5.0
@export var w: String = 'ab'

#func _ready() -> void:
	#var c = test
	#print(c.call(1, 2))
	#print(TileSet.CELL_NEIGHBOR_BOTTOM_CORNER)
	#var t = TileSet.new()
	#print(t.CELL_NEIGHBOR_BOTTOM_CORNER)
	#print(TYPE_BOOL)

func test(a: int, b: float):
	return a + b

func _process(delta: float) -> void:
	pass

func _on_py_node_health_changed(old_value: Variant, new_value: Variant) -> void:
	print('_on_py_node_health_changed', old_value, new_value)
