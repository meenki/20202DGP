from pico2d import *
import gfw
from enemy import *

class Dice:
	def __init__(self, pos, style, num, lv):
		self.pos = pos
		self.default = pos
		self.style = style
		self.lv = lv
		self.attacksp = 1 / self.lv
		self.elapsed = 0
		self.num = num

		imageName = None
		if style == 'fast':
			imageName = 'fast'
			self.attacksp = self.attacksp * 0.3
		elif style == 'slow':
			imageName = 'slow'
		elif style == 'multi':
			imageName = 'multi'

		self.image = gfw.image.load('res/' + imageName + str(lv) + '.png')
		self.w = self.image.w
		self.h = self.image.h

	def update(self):
		if gfw.state != 'start':
			return

		self.elapsed += gfw.delta_time

		if self.elapsed > self.attacksp:
			self.attack()
			self.elapsed = 0

	def draw(self):
		self.image.draw(*self.pos)

	def attack(self):
		if gfw.world.count_at(gfw.layer.enemy) > 0:
			generator_bullet(self)

	def drag(self, pos):
		self.pos = pos

	def setdefault(self):
		self.pos = self.default

	def collision(self, pos):
		x, y = self.pos
		tx, ty = pos

		l, r, t, b = x - self.w//2, x + self.w//2, y - self.h//2, y + self.h//2

		if (tx > l) and (tx < r) and (ty > t) and (ty < b):
			return self.style
		else :
			return False

def generator_bullet(target):
	if target.style == 'multi':
		count = 0
		for e in gfw.world.objects_at(gfw.layer.enemy):
			if count >= target.lv * 2 or count > gfw.world.count_at(gfw.layer.enemy):
				return
			count += 1
			b = bullet(target.pos, target.style, target.lv, e)
			gfw.world.add(gfw.layer.enemy, b)


	b = bullet(target.pos, target.style, target.lv, gfw.world.object(gfw.layer.enemy, 0))
	gfw.world.add(gfw.layer.enemy, b)


class bullet:
	def __init__(self, pos, style, lv, target = None):
		self.pos = pos
		self.prepos = self.pos
		self.style = style
		self.lv = lv
		self.image = gfw.image.load('res/bullet.png')

		self.hitsound = load_wav('res/hit.wav')
		self.hitsound.set_volume(15)
		self.hitsound.play()

		if isinstance(target, Enemy):
			self.target = target
		else:
			self.target = gfw.world.object(gfw.layer.enemy, 0)
		self.elapsed = 0

		if not isinstance(target, Enemy):
			gfw.world.remove(self)
			return

	def update(self):
		if gfw.state != 'start':
			return
		if not isinstance(self.target, Enemy):
			gfw.world.remove(self)
			pass

		self.elapsed += gfw.delta_time

		speed = 2

		x, y = self.prepos
		tx, ty = self.target.pos

		x = lerp(x, tx, self.elapsed * speed)
		y = lerp(y, ty, self.elapsed * speed)
			
		self.pos = (x, y)

		if self.elapsed > 0.5:
			self.target.hit(self.style, self.lv)
			gfw.world.remove(self)

	def draw(self):
		self.image.draw(*self.pos)

def lerp(a, b, delta) :
	return a * (1 - delta) + b * delta