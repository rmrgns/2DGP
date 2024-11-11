from pico2d import * 
import gfw
import upgrade_scene
import end_scene

from fighter import Fighter
from enemy import EnemyGen
from turret import Turret

world = gfw.World(['bg', 'fighter', 'bullet', 'enemy', 'ui', 'controller', 'turret'])

canvas_width = 500
canvas_height = 800
shows_bounding_box = True
shows_object_count = True

def enter():
    global turrets
    turrets = []
    for i in range(1,6):
        x,y = i*100-50, 200
        turret = Turret(x,y)
        turrets.append(turret)
        world.append(turret,world.layer.turret)
    for i in range(1,6):
        x, y = i * 100 - 50, 100
        turret = Turret(x, y)
        turrets.append(turret)
        world.append(turret, world.layer.turret)

    #center = world.append(gfw.Sprite('resources/center.png', 0, 0), world.layer.ui)
    world.append(gfw.VertFillBackground('res/clouds.png', -60), world.layer.bg)
    world.append(gfw.VertFillBackground('res/bg_city.png', -30), world.layer.bg)

    global fighter
    fighter = Fighter()
    # world.append(fighter, world.layer.fighter)
    # world.append(MainSceneUI(), world.layer.ui)
    global score_sprite
    score_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width - 50, canvas_height - 50)
    world.append(score_sprite, world.layer.ui)
    world.append(EnemyGen(), world.layer.controller)
    world.append(CollisionChecker(), world.layer.controller)


    global score
    score = 0

def exit():
    world.clear()
    print('[game.exit()]')

def pause():
    print('[game.pause()]')

def resume():
    print('[game.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
    if e.type == SDL_KEYDOWN and e.key == SDLK_s:
        world.append(fighter, world.layer.fighter)
    if e.type == SDL_KEYDOWN and e.key == SDLK_q:
        gfw.change(upgrade_scene)
    if e.type == SDL_KEYDOWN and e.key == SDLK_e:
        gfw.change(end_scene)
    fighter.handle_event(e)
    for turret in turrets:
        turret.handle_event(e)

class CollisionChecker:
    def draw(self): pass
    def update(self):
        enemies = world.objects_at(world.layer.enemy)
        for e in enemies: # reversed order
            collided = False
            bullets = world.objects_at(world.layer.bullet)
            for b in bullets: # reversed order
                if gfw.collides_box(b, e):
                    collided = True
                    world.remove(b)
                    dead = e.decrease_life(b.power)
                    if dead:
                        global score
                        score += e.score
                        score_sprite.score = score
                        # print(f'+{e.score} ={score}')
                        world.remove(e)
                    break
            if collided: break
            if gfw.collides_box(fighter, e):
                world.remove(e)
                # decrease fighter HP here?
                break

class GameScenUI:
    def __init__(self):
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)
    def update(self): pass
    def draw(self):
        self.font.draw(*self.pos, f'{score:10d}')


#if __name__ == '__main__':
#    gfw.start_main_module()

