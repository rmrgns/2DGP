from pico2d import *
import gfw
import main_scene
from button import Button
import playerstatus

world = gfw.World(['bg', 'button', 'ui'])
canvas_width = 700
canvas_height = 800

def enter():
    world.append(gfw.VertFillBackground('resources/spacebg.png', -30), world.layer.bg)

    global endbtn
    endbtn = Button('resources/gameover.png', canvas_width / 2, canvas_height * (1 / 4))
    world.append(endbtn, world.layer.button)

    global score_sprite
    score_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width / 2, canvas_height - 400)
    world.append(score_sprite, world.layer.ui)
    score_sprite.score = playerstatus.status.score
    score_text_sprite = gfw.Sprite('resources/score.png', canvas_width / 2 - 30, canvas_height - 400 + 45)
    world.append(score_text_sprite, world.layer.ui)

def exit():
    world.clear()
    playerstatus.status.__init__()
    print('[end.exit()]')

def pause():
    print('[end.pause()]')

def resume():
    print('[end.resume()]')

def handle_event(e):
    if e.type == SDL_MOUSEBUTTONDOWN:
        x, y = e.x, get_canvas_height() - e.y
        if endbtn.is_clicked(x, y):  # 클릭된 빈 공간이나 터렛 확인
            if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                gfw.pop()
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

