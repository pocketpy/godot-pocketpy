from godot import *

import test

class MyScript(Extends(Node)):
	x = export(int, default=10)
	y = export(Node)
	z = export_range(1.2, 10.2, 0.1, default=5)
	w = export(str, default='ab')
	
	health_changed = signal('old_value', 'new_value')

	def __init__(self):
		print('__init__()', TYPE_BOOL)
		print(TileSet.TILE_LAYOUT_STACKED_OFFSET)
		print('==>', test.add('hello', ' world'))
		#print("==>", self.x, self.y, self.z, self.w)

	def _ready(self):
		print('_ready()')
		print('==>', self.owner, self.owner.script)
		print('==>', self.x, self.y, self.z, self.w)
		print('==> path:', self.owner.get_path())
		
		self.health_changed.emit(100, 200)

	def _process(self, delta: float) -> None:
		return
		print('==>', f'_process({delta:.4f})')
