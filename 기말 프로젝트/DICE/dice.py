from pico2d import *
import gfw

class Dice:
	def __init__(self, imageName, pos, type):
		self.time = get_time()
		self.image = gfw.image.load(RES_DIR + '/' + imageName)
		self.pos = pos
		self.fps = 8
		if fcount == 0:
			fcount = self.image.w // self.image.h

		self.width = self.image.w // fcount
		self.height = self.image.h
		self.fcount = fcount

	def update(self):
		pass
		
	def draw(self):
		elapsed = get_time() - self.time
		fidx = round(elapsed * self.fps) % self.fcount
		sx = self.width * fidx
		size = self.width * self.mag, self.height * self.mag
		self.image.clip_draw(sx, 0, self.width, self.height, *self.pos, *size)