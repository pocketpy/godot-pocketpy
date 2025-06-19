from godot import Node, export, Extends

class MyScript(Extends(Node)):
	x = export(int, default=10)
	y = export(Node)
