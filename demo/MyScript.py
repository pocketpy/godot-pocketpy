from godot import Node, export, Extends

class MyScript(Extends(Node)):
	x = export(int, default=10)
	y = export(Node)
	z = export(float, default=2.0)
	w = export(str, default='abc')
