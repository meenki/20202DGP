from pico2d import *
import gfw
from button import Button

def init():
	global background, gray, board, line, coin, upgrade
	global start, pause, multiup, fastup, slowup, newdice, exit, restart

	global state

	background = gfw.image.load('res/white.png')
	gray = gfw.image.load('res/graycover.png')
	board = gfw.image.load('res/board.png')
	line = gfw.image.load('res/line.png')
	coin = gfw.image.load('res/coin.png')
	upgrade = gfw.image.load('res/upgrade.png')

	global test
	test = gfw.image.load('res/multi1.png')

	start = Button('start.png', (get_canvas_width() // 2, get_canvas_height()//2 + 285), 'start')
	pause = Button('pause.png', (get_canvas_width() // 2, get_canvas_height()//2 + 285), 'pause')

	exit = Button('exit.png', (get_canvas_width() // 2 - 100, get_canvas_height()//2 + 285), 'exit')
	restart = Button('restart.png', (get_canvas_width() // 2 + 100, get_canvas_height()//2 + 285), 'restart')

	slowup = Button('slowup.png', (get_canvas_width() // 2, get_canvas_height()//2 - 400), 'slowup')
	fastup = Button('fastup.png', (get_canvas_width() // 2 - 170, get_canvas_height()//2 - 400), 'fastup')
	multiup = Button('multiup.png', (get_canvas_width() // 2 + 170, get_canvas_height()//2 - 400), 'multiup')

	newdice = Button('newdice.png', (get_canvas_width() // 2, get_canvas_height()//2 - 270), 'newdice')

	state = 'stop'

def draw():
	background.draw(get_canvas_width() // 2, get_canvas_height() // 2)
	gray.draw(get_canvas_width() // 2, get_canvas_height() - 70)
	board.draw(get_canvas_width() // 2, get_canvas_height()//2 + 30)
	line.draw(get_canvas_width() // 2, get_canvas_height()//2 + 80)

	coin.draw(get_canvas_width() // 2 - 180, get_canvas_height()//2 - 300)
	coin.draw(get_canvas_width() // 2 - 20, get_canvas_height()//2 - 315)
	coin.draw(get_canvas_width() // 2 - 180, get_canvas_height()//2 - 440)
	coin.draw(get_canvas_width() // 2 - 10, get_canvas_height()//2 - 440)
	coin.draw(get_canvas_width() // 2 + 160, get_canvas_height()//2 - 440)

	if gfw.state == 'stop' or gfw.state == 'over':
		start.draw()
		exit.draw()
	elif gfw.state == 'start':
		pause.draw()
	elif gfw.state == 'pause':
		start.draw()
		exit.draw()
		restart.draw()

	multiup.draw()
	fastup.draw()
	slowup.draw()
	newdice.draw()

	upgrade.draw(get_canvas_width() // 2 - 180, get_canvas_height()//2 - 398)
	upgrade.draw(get_canvas_width() // 2 - 10, get_canvas_height()//2 - 398)
	upgrade.draw(get_canvas_width() // 2 + 160, get_canvas_height()//2 - 398)

def update():
	pass

def click(pos):
	if gfw.state == 'stop' or gfw.state == 'over':
		if start.click(pos) != None:
			return 'start'
		if exit.click(pos) != None:
			return 'exit'
	elif gfw.state == 'pause':
		if start.click(pos) != None:
			return 'start'
		if exit.click(pos) != None:
			return 'exit'
		if restart.click(pos) != None:
			return 'restart'
	elif gfw.state == 'start':
		if pause.click(pos) != None:
			return 'pause'
		if multiup.click(pos) != None:
			return 'multiup'
		if fastup.click(pos) != None:
			return 'fastup'
		if slowup.click(pos) != None:
			return 'slowup'
		if newdice.click(pos) != None:
			return 'newdice'