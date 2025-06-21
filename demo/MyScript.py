from godot import *

class MyScript(Extends(Node)):
	x = export(int, default=10)
	y = export(Node)
	z = export_range(1.2, 10.2, 0.1, default=5)
	w = export(str, default='ab')

	def _ready(self):
		print("_ready")
