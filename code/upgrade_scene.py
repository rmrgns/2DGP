from pico2d import *
import gfw

from button import Button
import playerstatus

world = gfw.World(['upgradebg', 'button'])
canvas_width = 700
canvas_height = 800

def enter():
    world.append(gfw.Background('resources/spacebg.png'), world.layer.upgradebg)

    global fighterHPUpgradeBtn
    fighterHPUpgradeBtn = Button('resources/gamestart.png', canvas_width / 2, canvas_height * (3 / 4))
    world.append(fighterHPUpgradeBtn, world.layer.button)

    global shieldTurretHPUpgradeBtn
    shieldTurretHPUpgradeBtn = Button('resources/gamestart.png', canvas_width / 2, canvas_height * (2 / 4))
    world.append(shieldTurretHPUpgradeBtn, world.layer.button)

    global gunTurretATKUpgradeBtn
    gunTurretATKUpgradeBtn = Button('resources/gamestart.png', canvas_width / 2, canvas_height * (1 / 4))
    world.append(gunTurretATKUpgradeBtn, world.layer.button)
    pass

def exit():
    world.clear()
    print('[upgrade.exit()]')

def pause():
    print('[upgrade.pause()]')

def resume():
    print('[upgrade.resume()]')

def handle_event(e):
    global fighterHPUpgradeBtn
    global shieldTurretHPUpgradeBtn
    global gunTurretATKUpgradeBtn

    if e.type == SDL_KEYDOWN:
        gfw.change(game_scene)

    if e.type == SDL_MOUSEBUTTONDOWN:
        x, y = e.x, get_canvas_height() - e.y
        if fighterHPUpgradeBtn.is_clicked(x, y):  # 클릭된 빈 공간이나 터렛 확인
            if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                playerstatus.status.upgradefighterHP()

        if shieldTurretHPUpgradeBtn.is_clicked(x, y):
            if e.button == SDL_BUTTON_LEFT:
                playerstatus.status.upgradeshieldturretHP()

        if gunTurretATKUpgradeBtn.is_clicked(x, y):
            if e.button == SDL_BUTTON_LEFT:
                playerstatus.status.upgradegunturreATK()


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

