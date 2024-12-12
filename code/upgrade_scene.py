import time

from pico2d import *
import gfw

from button import Button
import playerstatus
import game_scene

world = gfw.World(['upgradebg', 'button', 'ui'])
canvas_width = 700
canvas_height = 800

def enter():
    world.append(gfw.Background('resources/spacebg.png'), world.layer.upgradebg)

    global fighterHPUpgradeBtn
    global fighterHP_sprite
    fighterHPUpgradeBtn = Button('resources/upFHP.png', canvas_width * (1 / 3), canvas_height * (5 / 6))
    world.append(fighterHPUpgradeBtn, world.layer.button)
    fighterHP_sprite = gfw.ScoreSprite('resources/number_24x32.png', canvas_width * (2 / 3), canvas_height * (5 / 6))
    world.append(fighterHP_sprite, world.layer.ui)
    fighterHP_sprite.score = playerstatus.status.getfighterHPUpgrade()

    global fighterATKUpgradeBtn
    global fighterATK_sprite
    fighterATKUpgradeBtn = Button('resources/upFATK.png', canvas_width * (1 / 3), canvas_height * (4 / 6))
    world.append(fighterATKUpgradeBtn, world.layer.button)
    fighterATK_sprite = gfw.ScoreSprite('resources/number_24x32.png', canvas_width * (2 / 3), canvas_height * (4 / 6))
    world.append(fighterATK_sprite, world.layer.ui)
    fighterATK_sprite.score = playerstatus.status.getfighterATKUpgrade()


    global shieldTurretHPUpgradeBtn
    global shieldTurretHP_sprite
    shieldTurretHPUpgradeBtn = Button('resources/upSHP.png', canvas_width * (1 / 3), canvas_height * (3 / 6))
    world.append(shieldTurretHPUpgradeBtn, world.layer.button)
    shieldTurretHP_sprite = gfw.ScoreSprite('resources/number_24x32.png', canvas_width * (2 / 3), canvas_height * (3 / 6))
    world.append(shieldTurretHP_sprite, world.layer.ui)
    shieldTurretHP_sprite.score = playerstatus.status.getshieldturretHPUpgrade()

    global gunTurretATKUpgradeBtn
    global gunTurretATK_sprite
    gunTurretATKUpgradeBtn = Button('resources/upGATK.png', canvas_width * (1 / 3), canvas_height * (2 / 6))
    world.append(gunTurretATKUpgradeBtn, world.layer.button)
    gunTurretATK_sprite = gfw.ScoreSprite('resources/number_24x32.png', canvas_width * (2 / 3), canvas_height * (2 / 6))
    world.append(gunTurretATK_sprite, world.layer.ui)
    gunTurretATK_sprite.score = playerstatus.status.getgunturretATKUpgrade()

    global gameStartBtn
    gameStartBtn = Button('resources/gamestart.png', canvas_width * (1 / 3), canvas_height * (1 / 6))
    world.append(gameStartBtn, world.layer.button)

    global gold_sprite
    gold_sprite = gfw.ScoreSprite('resources/number_24x32.png', canvas_width - 50, canvas_height - 100)
    world.append(gold_sprite, world.layer.ui)
    gold_sprite.score = playerstatus.status.gold


def exit():
    game_scene.getGold_scoreBtn().score = playerstatus.status.gold
    playerstatus.status.roundstarttime = time.time()
    playerstatus.status.round += 1
    playerstatus.status.gold = playerstatus.status.round * 200
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

    if e.type == SDL_MOUSEBUTTONDOWN:
        x, y = e.x, get_canvas_height() - e.y
        if playerstatus.status.upgradeCheck():
            if fighterHPUpgradeBtn.is_clicked(x, y):
                if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                    playerstatus.status.upgradefighterHP()
                    fighterHP_sprite.score = playerstatus.status.getfighterHPUpgrade()

            if fighterATKUpgradeBtn.is_clicked(x, y):
                if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                    playerstatus.status.upgradefighterATK()
                    fighterATK_sprite.score = playerstatus.status.getfighterATKUpgrade()

            if shieldTurretHPUpgradeBtn.is_clicked(x, y):
                if e.button == SDL_BUTTON_LEFT:
                    playerstatus.status.upgradeshieldturretHP()
                    shieldTurretHP_sprite.score = playerstatus.status.getshieldturretHPUpgrade()

            if gunTurretATKUpgradeBtn.is_clicked(x, y):
                if e.button == SDL_BUTTON_LEFT:
                    playerstatus.status.upgradegunturreATK()
                    gunTurretATK_sprite.score = playerstatus.status.getgunturretATKUpgrade()


            gold_sprite.score = playerstatus.status.gold

        if gameStartBtn.is_clicked(x, y):
            if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                gfw.change(game_scene)
                # gfw.pop()


class CollisionChecker:
    def draw(self): pass
    def update(self):
        pass

class GameScenUI:
    def __init__(self):
        self.font = load_font('resources/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)
    def update(self): pass
    def draw(self):
        #self.font.draw(*self.pos, f'{score:10d}')
        pass

