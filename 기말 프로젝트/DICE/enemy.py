from pico2d import *
import gfw

LIFE_TEXT_COLOR = (0, 0, 0)

class Enemy:
	def __init__(self, lv):
		self.pos = 57, 820
		self.life = lv * 10
		self.image = gfw.image.load('res/enemy.png')

		self.state = 1
		self.target = 1

		self.speed = 100

		self.dead = False

		self.font = gfw.font.load('res/ConsolaMalgun.ttf', 15)

	def update(self):
		if gfw.state != 'start':
			return

		x, y = self.pos

		if self.target == 1:
			y -= self.speed * gfw.delta_time * self.state
			if y < 304:
				y = 304
				self.target = 2
		elif self.target == 2:
			x += self.speed * gfw.delta_time * self.state
			if x > 482:
				x = 482
				self.target = 3
		elif self.target == 3:
			y += self.speed * gfw.delta_time * self.state
			if y > 820:
				y = 820
				self.target = 4
		else :
			gfw.state = 'over'

		self.pos = (x, y)

	def draw(self):
		self.image.draw(*self.pos)
		self.font.draw(self.pos[0] - 30, self.pos[1] + 15, '%d' % self.life, LIFE_TEXT_COLOR)

	def hit(self, style, lv):
		if self.dead:
			return

		damage = lv

		if style == 'slow':
			self.state = min(self.state, 1 / (lv * 2))
			damage += gfw.slowup ** lv
		elif style == 'fast':
			damage += gfw.fastup ** lv
		elif style == 'multi':
			damage += gfw.multiup ** lv

		self.life -= lv

		if self.life <= 0:
			gfw.coin += 10
			gfw.world.remove(self)
			self.dead = True