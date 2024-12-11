from pico2d import * 
import gfw
import upgrade_scene
import end_scene
import playerstatus

from fighter import Fighter
from enemy import EnemyGen
from turret import Turret
from commandcenter import CmdCenter

world = gfw.World(['bg', 'fighter', 'bullet', 'enemy', 'ui', 'controller', 'turret', 'center', 'enemybullet'])

canvas_width = 500
canvas_height = 800
shows_bounding_box = True
shows_object_count = False



def enter():
    #center = world.append(gfw.Sprite('resources/center.png', 0, 0), world.layer.ui)
    #world.append(gfw.VertFillBackground('resources/stars2.png', -60), world.layer.bg)
    world.append(gfw.VertFillBackground('resources/battlebg.png', -30), world.layer.bg)

    ui_sprite = gfw.Sprite('resources/gameui.png', canvas_width + 100, canvas_height / 2)
    world.append(ui_sprite, world.layer.ui)



    global fighter
    fighter = Fighter()
    world.append(fighter, world.layer.fighter)
    # world.append(MainSceneUI(), world.layer.ui)

    global score_sprite
    score_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width + 150, canvas_height - 100)
    world.append(score_sprite, world.layer.ui)
    score_sprite.score = playerstatus.status.score
    score_text_sprite = gfw.Sprite('resources/score.png', canvas_width + 120, canvas_height - 100 + 35)
    world.append(score_text_sprite, world.layer.ui)

    global gold_sprite
    gold_sprite = gfw.ScoreSprite('res/number_24x32.png', canvas_width + 150, canvas_height - 200)
    world.append(gold_sprite, world.layer.ui)
    gold_sprite.score = playerstatus.status.gold
    gold_text_sprite = gfw.Sprite('resources/gold.png', canvas_width + 110, canvas_height - 200 + 50)
    world.append(gold_text_sprite, world.layer.ui)

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

    global center
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
        self.enemyAttack()
        self.playerAttack()
    def enemyAttack(self):
        enemybullets = world.objects_at(world.layer.enemybullet)
        for eb in enemybullets:
            turrets = world.objects_at(world.layer.turret)
            for t in turrets:
                if gfw.collides_box(t, eb):
                    if t.turret_type == 0:
                        pass
                    else:
                        world.remove(eb)
                        sdead = t.dead(eb.power)
                        if sdead:
                            t.to_empty_space()
            if gfw.collides_box(fighter, eb):
                if fighter.operating:
                    world.remove(eb)
                    fdead = fighter.dead()
                    if fdead:
                        fighter.operating = False
            if gfw.collides_box(center, eb):
                if center.dead(eb.power):
                    # gfw.pop()
                    print("center attacked")
                world.remove(eb)


    def playerAttack(self):
        enemies = world.objects_at(world.layer.enemy)
        for e in enemies:  # reversed order
            collided = False
            bullets = world.objects_at(world.layer.bullet)
            for b in bullets:  # reversed order
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

            if gfw.collides_box(fighter, e):
                if fighter.operating:
                    collided = True
                    world.remove(e)
                    fdead = fighter.dead()
                    if fdead:
                        fighter.operating = False
                        print("fighter dead")

            turrets = world.objects_at(world.layer.turret)
            for t in turrets:
                if gfw.collides_box(t, e):
                    if t.turret_type == 0:
                        pass
                    else:
                        collided = True
                        world.remove(e)
                        sdead = t.dead(1)
                        if sdead:
                            t.to_empty_space()

            if gfw.collides_box(center, e):
                collided = True
                if center.dead(e.power):
                    gfw.push(end_scene)
                    print("center attacked")
                else:
                    world.remove(e)
            if collided: break



class GameScenUI:
    def __init__(self):
        self.font = load_font('res/lucon.ttf', 50)
        self.pos = (canvas_width - 320, canvas_height - 40)
    def update(self): pass
    def draw(self):
        self.font.draw(*self.pos, f'{playerstatus.status.gold:10d}')


#if __name__ == '__main__':
#    gfw.start_main_module()

