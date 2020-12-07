from pico2d import *
import gfw
import dice
import ui
import enemy
import generator

SCORE_TEXT_COLOR = (0, 0, 0)

def enter():
	global bl, br, bt, bb

	bl, br, bt, bb = get_canvas_width() // 2 - 170, get_canvas_width() // 2 + 170, get_canvas_height()//2 + 30 - 170, get_canvas_height()//2 + 30 + 170

	gfw.world.init(['ui', 'dice', 'bullet', 'enemy'])
	ui.init()
	generator.init()

	gfw.world.add(gfw.layer.ui, ui)

	global font, stagefont
	font = gfw.font.load('res/ConsolaMalgun.ttf', 15)
	stagefont = gfw.font.load('res/ConsolaMalgun.ttf', 40)

	global dicecost, fastcost, slowcost, multicost

	global isclick, target

	initgame()

	isclick = False
	target = None

	global buttonsound

	buttonsound = load_wav('res/button.wav')
	buttonsound.set_volume(15)

def exit():
	pass


def update():
	gfw.world.update()
	generator.update()

def draw():
	gfw.world.draw()
	fontdraw()

def mouse_down(e):
	global dicecost, fastcost, slowcost, multicost

	if e.button != SDL_BUTTON_LEFT:
		return

	mousePos = e.x, get_canvas_height() - e.y

	message = ui.click(mousePos)

	if message != None:
		buttonsound.play()

	if message == 'start':
		gfw.state = 'start'
		if gfw.state == 'stop' or gfw.state == 'over':
			initgame()
	elif message == 'pause':
		gfw.state = 'pause'
	elif message == 'restart':
		initgame()
		gfw.state = 'stop'
		initgame()
	elif message == 'exit':
		gfw.quit()

	if gfw.state == 'start':
		if message == 'slowup':
			if slowcost > gfw.coin:
				return
			gfw.coin -= slowcost
			slowcost+=100 *gfw.slowup
			gfw.slowup+=1
		elif message == 'fastup':
			if fastcost > gfw.coin:
				return
			gfw.coin -= fastcost
			fastcost+=100 *gfw.fastup
			gfw.fastup+=1
		elif message == 'multiup':
			if multicost > gfw.coin:
				return
			gfw.coin -= multicost
			multicost += 100 * gfw.multiup
			gfw.multiup+=1
		elif message == 'newdice':
			if gfw.coin < dicecost:
				return

			if generator.generator_dice():
				gfw.coin -= dicecost
				dicecost += 10
		else:
			collision_dice(mousePos)


def mouse_up(e):
	global isclick, target

	if not isclick:
		return

	mousePos = e.x, get_canvas_height() - e.y

	for d in gfw.world.objects_at(gfw.layer.dice):
		if d != target:
			if d.collision(mousePos) == target.style and d.lv == target.lv:
				generator.fusion_dice(target, d)
				isclick = False
				target = None
				return

	target.setdefault()
	isclick = False
	target = None

def collision_dice(e):
	global isclick, target

	for d in gfw.world.objects_at(gfw.layer.dice):
		if d.lv == 6:
			continue
		if d.collision(e):
			isclick = True
			target = d
			return


def handle_event(e):
	if e.type  == SDL_QUIT:
		gfw.quit()
	elif e.type == SDL_MOUSEBUTTONDOWN:
		mouse_down(e)
	elif e.type == SDL_MOUSEBUTTONUP:
		mouse_up(e)
	elif e.type == SDL_MOUSEMOTION:
		drag(e)

def drag(e):
	global isclick, target

	mousePos = e.x, get_canvas_height() - e.y

	if isclick:
		target.drag(mousePos)
		if not((mousePos[0] > bl) and (mousePos[0] < br) and (mousePos[1] > bt) and (mousePos[1] < bb)):
			target.setdefault()
			isclick = False
			target = None

def initgame():
	global dicecost, fastcost, slowcost, multicost
	global isclick, target

	gfw.state = 'stop'
	gfw.stagelv = 0

	gfw.coin = 100
	dicecost = 10
	gfw.fastup = 0
	gfw.slowup = 0
	gfw.multiup = 0
	fastcost = 100
	slowcost = 100
	multicost = 100

	isclick = False
	target = None

	for d in gfw.world.objects_at(gfw.layer.dice):
		gfw.world.remove(d)
	for d in gfw.world.objects_at(gfw.layer.bullet):
		gfw.world.remove(d)
	for d in gfw.world.objects_at(gfw.layer.enemy):
		gfw.world.remove(d)


def fontdraw():
	global dicecost, fastcost, slowcost, multicost

	font.draw(get_canvas_width() // 2 - 170, get_canvas_height()//2 - 300, '%d' % gfw.coin, SCORE_TEXT_COLOR)
	font.draw(get_canvas_width() // 2 - 10, get_canvas_height()//2 - 315, '%d' % dicecost, SCORE_TEXT_COLOR)

	font.draw(get_canvas_width() // 2 - 175, get_canvas_height()//2 - 400, '%d' % gfw.fastup, SCORE_TEXT_COLOR)
	font.draw(get_canvas_width() // 2 - 5, get_canvas_height()//2 - 400, '%d' % gfw.slowup, SCORE_TEXT_COLOR)
	font.draw(get_canvas_width() // 2 + 165, get_canvas_height()//2 - 400, '%d' % gfw.multiup, SCORE_TEXT_COLOR)

	font.draw(get_canvas_width() // 2 - 170, get_canvas_height()//2 - 440, '%d' % fastcost, SCORE_TEXT_COLOR)
	font.draw(get_canvas_width() // 2, get_canvas_height()//2 - 440, '%d' % slowcost, SCORE_TEXT_COLOR)
	font.draw(get_canvas_width() // 2 + 170, get_canvas_height()//2 - 440, '%d' % multicost, SCORE_TEXT_COLOR)

	if gfw.state == 'over':
		stagefont.draw(get_canvas_width() // 2, get_canvas_height() - 70, 'GAME OVER', SCORE_TEXT_COLOR)
	else:
		stagefont.draw(get_canvas_width() // 2, get_canvas_height() - 70, '%d' % gfw.stagelv, SCORE_TEXT_COLOR)


if __name__=='__main__':
    gfw.run_main()
