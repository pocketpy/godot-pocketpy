from godot import *

class MyScript(Extends(Node)):
	x = export(int, default=10)
	y = export(Node)
	z = export_range(5, 50, 1)
	w = export(str, default='ab')
