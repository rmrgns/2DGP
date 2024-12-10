from pico2d import * 
import gfw
import upgrade_scene
import end_scene
import playerstatus

from fighter import Fighter
from enemy import EnemyGen
from turret import Turret
from commandcenter import CmdCenter

world = gfw.World(['bg', 'fighter', 'bullet', 'enemy', 'ui', 'controller', 'turret', 'center'])

canvas_width = 500
canvas_height = 800
shows_bounding_box = True
shows_object_count = False



def enter():
    #center = world.append(gfw.Sprite('resources/center.png', 0, 0), world.layer.ui)
    world.append(gfw.VertFillBackground('res/clouds.png', -60), world.layer.bg)
    world.append(gfw.VertFillBackground('res/bg_city.png', -30), world.layer.bg)

    global fighter
    fighter = Fighter()
    world.append(fighter, world.layer.fighter)
    # world.append(MainSceneUI(), world.layer.ui)

    global score_sprite
    score_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width + 150, canvas_height - 100)
    world.append(score_sprite, world.layer.ui)
    score_sprite.score = playerstatus.status.score

    global gold_sprite
    gold_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width + 150, canvas_height - 200)
    world.append(gold_sprite, world.layer.ui)
    gold_sprite.score = playerstatus.status.gold

    world.append(EnemyGen(), world.layer.controller)
    world.append(CollisionChecker(), world.layer.controller)

    for i in range(1,6):
        x,y = i*100-50, 200
        turret = Turret(x,y)
        world.append(turret,world.layer.turret)
    for i in range(1,6):
        x, y = i * 100 - 50, 100
        turret = Turret(x, y)
        world.append(turret, world.layer.turret)

    center = CmdCenter(canvas_width / 2, 10)
    world.append(center, world.layer.center)

def exit():
    world.clear()
    print('[game.exit()]')

def pause():
    print('[game.pause()]')

def resume():
    print('[game.resume()]')

def handle_event(e):
    global fighter
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
    if e.type == SDL_KEYDOWN and e.key == SDLK_s:
        if fighter.operating == False:
            # fighter = Fighter()
            # world.append(fighter, world.layer.fighter)
            # fighter_count = True
            fighter.__init__()
            fighter.operating = True

    if e.type == SDL_KEYDOWN and e.key == SDLK_q:
        gfw.push(upgrade_scene)
    if e.type == SDL_KEYDOWN and e.key == SDLK_e:
        gfw.change(end_scene)
    if e.type == SDL_KEYDOWN and e.key == SDLK_t:
        for i, objs in enumerate(world.objects):
            print(f"Layer {i}: {objs}")
    # 전투기 이벤트
    if fighter.operating == True:
        fighter.handle_event(e)
    # 터렛 이벤트
    turrets = world.objects_at(world.layer.turret)
    for t in turrets:
        t.handle_event(e)

def getGold_scoreBtn():
    global gold_sprite
    return gold_sprite


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
                        playerstatus.status.score += e.score
                        score_sprite.score = playerstatus.status.score

                        playerstatus.status.gold += e.score
                        gold_sprite.score = playerstatus.status.gold
                        # print(f'+{e.score} ={score}')
                        world.remove(e)
                    break
            if collided: break
            if gfw.collides_box(fighter, e):
                world.remove(e)
                fdead = fighter.dead()
                if fdead:
                    fighter.operating = False
                    print("fighter dead")

            turrets = world.objects_at(world.layer.turret)
            for t in turrets:
                if gfw.collides_box(t,e):
                    if t.turret_type == 0:
                        pass
                    else:
                        collided = True
                        world.remove(e)
                        sdead = t.dead()
                        if sdead:
                            t.to_empty_space()


class GameScenUI:
    def __init__(self):
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)
    def update(self): pass
    def draw(self):
        self.font.draw(*self.pos, f'{playerstatus.status.gold:10d}')


#if __name__ == '__main__':
#    gfw.start_main_module()

