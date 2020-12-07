from pico2d import *
import gfw
import random
from dice import Dice
from enemy import Enemy

boardstate = [0] * 25
enemycount = 0
move = 59.3

spawntime = 1

dicestyle = ['fast', 'slow', 'multi']

def init():
	global elapsed
	global newdice

	newdice = load_wav('res/newdice.wav')
	newdice.set_volume(15)

	elapsed = 0
	pass

def update():
	global elapsed, enemycount
	if gfw.state != 'start':
		return

	elapsed += gfw.delta_time

	if enemycount == gfw.stagelv and gfw.world.count_at(gfw.layer.enemy) == 0:
		enemycount = 0
		gfw.coin += gfw.stagelv * 10
		gfw.stagelv += 1

	if enemycount < gfw.stagelv:
		if elapsed > spawntime:
			generator_enemy()
			elapsed = 0

def generator_enemy():
	global enemycount

	e = Enemy(gfw.stagelv)
	gfw.world.add(gfw.layer.enemy, e)
	enemycount += 1

def generator_dice(style = None, num = None, lv = 1):
	while gfw.world.count_at(gfw.layer.dice) < 25:
		if num == None:	
			num = random.randrange(25)
		if style == None:
			style = random.choice(dicestyle)

		if boardstate[num] == 0:
			d = Dice((get_canvas_width() // 2 - 118.6 + move * (num%5), get_canvas_height()//2 + 155.9 - move * (num//5)),
			 style,
			 num,
			 lv)

			gfw.world.add(gfw.layer.dice, d)
			boardstate[num] = 1

			newdice.play()

			return True
		else:
			num = None
			continue

	return False

def fusion_dice(lhs, rhs):
	num = rhs.num
	style = rhs.style
	lv = rhs.lv + 1

	boardstate[lhs.num] = 0
	boardstate[rhs.num] = 0

	gfw.world.remove(lhs)
	gfw.world.remove(rhs)

	gfw.world.update()

	generator_dice(None, num, lv)