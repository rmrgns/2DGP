from pico2d import *
import gfw
import game_scene
from button import Button

world = gfw.World(['mainbg', 'button'])
canvas_width = 700
canvas_height = 800

bgm = None
click_sound = None

def enter():
    world.append(gfw.VertFillBackground('resources/spacebg.png', -30), world.layer.mainbg)

    title = gfw.Sprite('resources/title.png', canvas_width / 2, canvas_height * (3/4))
    world.append(title,world.layer.button)

    global startbtn
    startbtn = Button('resources/gamestart.png', canvas_width / 2, canvas_height * (1/4))
    world.append(startbtn,world.layer.button)

    global bgm, click_sound
    bgm = load_music('resources/Ascence.mp3')
    bgm.set_volume(4)
    bgm.repeat_play()

    click_sound = load_wav('resources/click.wav')
    click_sound.set_volume(16)

def exit():
    world.clear()
    print('[main.exit()]')

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN:
        print(world.objects)
        gfw.change(game_scene)
    global startbtn
    if e.type == SDL_MOUSEBUTTONDOWN:
        x, y = e.x, get_canvas_height() - e.y
        if startbtn.is_clicked(x, y):  # 클릭된 빈 공간이나 터렛 확인
            if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                click_sound.play()
                gfw.push(game_scene)

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


if __name__ == '__main__':
    gfw.start_main_module()