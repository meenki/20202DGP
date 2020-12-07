from pico2d import *
import gfw

class Button:
	def __init__(self, imageName, pos, style):
		self.image = gfw.image.load('res/' + imageName)
		self.pos = pos
		self.style = style
		self.w = self.image.w;
		self.h = self.image.h;

	def draw(self):
		self.image.draw(*self.pos)

	def update(self):
		pass

	def click(self, pos):
		if self.check_collision(pos):
			if self.style == 'start':
				return 'start'
			elif self.style == 'pause':
				return 'pause'
			elif self.style == 'slowup':
				return 'slowup'
			elif self.style == 'fastup':
				return 'fastup'
			elif self.style == 'multiup':
				return 'multiup'
			elif self.style == 'newdice':
				return 'newdice'
			elif self.style == 'restart':
				return 'restart'
			elif self.style == 'exit':
				return 'exit'

		return None

	def check_collision(self, pos):
		x, y = self.pos
		tx, ty = pos

		l, r, t, b = x - self.w//2, x + self.w//2, y - self.h//2, y + self.h//2

		return (tx > l) and (tx < r) and (ty > t) and (ty < b)