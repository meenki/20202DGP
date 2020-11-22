from pico2d import *
import helper

class Boy:
    def __init__(self):
        self.image = load_image('res/run_animation.png')
        self.fidx = 1
        self.speed = 1
        self.delta = 0.8
        self.target = None
        self.pos = 0, 90

    def Draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100,
                             self.pos[0], self.pos[1])

    def Update(self):
        self.fidx=(self.fidx + 1) % 8
        helper.move_toward_obj(boy)
        
        if self.target == None:
            self.speed = 1

def handle_events():

    global running
    global boy

    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            running = False
            
        elif e.type == SDL_MOUSEBUTTONDOWN:
            helper.set_target(boy, (e.x, 600-1-e.y))
            
            boy.speed += 1
            
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            running = False
            
open_canvas()

boy = Boy()
running = True
gra = load_image('res/grass.png')


while running:
    clear_canvas()
    
    gra.draw(400,30)
    boy.Draw()
    
    update_canvas()
    
    boy.Update()
    
    handle_events()

    delay(0.01)

close_canvas()
