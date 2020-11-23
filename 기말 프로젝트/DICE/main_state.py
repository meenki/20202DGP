from pico2d import *
import gfw
import dice
import ui
import enemy

def enter():
	gfw.world.init(['UI', 'player', 'enemy'])

def exit():
	pass

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

def KeyDown(k):
	if k == SDLK_ESCAPE:
		gfw.pop()

def Mouse(e):
	global mousePos
	if e.button != SDL_BUTTON_LEFT:
		print('fuck')


		

	mousePos = e.x, e.y

	print(mousePos)

def handle_event(e):
    if e.type  == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
    	KeyDown(e.key)
    elif e.type == SDL_MOUSEBUTTONDOWN:
    	Mouse(e)

if __name__=='__main__':
    gfw.run_main()
