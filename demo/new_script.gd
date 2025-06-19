extends Node

func _enter_tree() -> void:
	pass

func _ready():
	var x = Node
	print(type_string(typeof(x)), x)
	return 'test'


func _on_node_ready2() -> void:
	print(Resource)
