from godot import *

class MyScript(Extends(Node)):
	x = export(int, default=10)
	y = export(Node)
	z = export_range(1.2, 10.2, 0.1, default=5)
	w = export(str, default='ab')

	def __init__(self):
		print("__init__()")
		#print("==>", self.x, self.y, self.z, self.w)

	def _ready(self):
		print('_ready()')
		print('==>', self.x, self.y, self.z, self.w)
		print('==> path:', self.owner.get_path())

	def _process(self, delta: float) -> None:
		print('==>', f'_process({delta:.4f})')
