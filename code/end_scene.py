from pico2d import *
import gfw
import main_scene

world = gfw.World(['mainbg'])
canvas_width = 500
canvas_height = 800

def enter():
    pass

def exit():
    world.clear()
    print('[end.exit()]')

def pause():
    print('[end.pause()]')

def resume():
    print('[end.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN:
        print(world.objects)
        gfw.pop()


class CollisionChecker:
    def draw(self): pass
    def update(self):
        pass

class GameScenUI:
    def __init__(self):
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)
    def update(self): pass
    def draw(self):
        #self.font.draw(*self.pos, f'{score:10d}')
        pass

