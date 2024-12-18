from pico2d import *
import gfw
import playerstatus
import time
import game_scene

class Fighter(gfw.Sprite):
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_a):  -1,
        (SDL_KEYDOWN, SDLK_d):  1,
        (SDL_KEYUP, SDLK_a):     1,
        (SDL_KEYUP, SDLK_d):   -1,
        (SDL_KEYDOWN, SDLK_s): -1,
        (SDL_KEYDOWN, SDLK_w): 1,
        (SDL_KEYUP, SDLK_s): 1,
        (SDL_KEYUP, SDLK_w): -1,
        (SDL_KEYDOWN, SDLK_SPACE): 1,
        (SDL_KEYUP, SDLK_SPACE): 0,
    }
    LASER_INTERVAL = 0.25
    SPARK_INTERVAL = 0.05
    SPARK_OFFSET = 28
    MAX_ROLL = 0.4
    IMAGE_RECTS = [
        (  8, 0, 42, 80),
        ( 76, 0, 42, 80),
        (140, 0, 50, 80),
        (205, 0, 56, 80),
        (270, 0, 62, 80),
        (334, 0, 70, 80),
        (406, 0, 62, 80),
        (477, 0, 56, 80),
        (549, 0, 48, 80),
        (621, 0, 42, 80),
        (689, 0, 42, 80),
    ]
    WIDTH = 100
    gauge = None

    def __init__(self):
        super().__init__('resources/fighters.png', (get_canvas_width()-200) // 2, 80)
        self.dx = 0
        self.dy = 0
        self.speed = 320 # 320 pixels per second
        self.width = 72
        self.height = 200
        half_width = self.width // 2
        half_height = self.height // 2
        self.min_x = half_width
        self.max_x = get_canvas_width()-200 - half_width
        self.min_y = half_height
        self.max_y = get_canvas_height() - half_height
        self.laser_time = 0
        self.spark_image = gfw.image.load('resources/laser_0.png')
        self.roll_time = 0
        self.src_rect = Fighter.IMAGE_RECTS[5] # 0~10 의 11 개 중 5번이 가운데이다.
        self.operating = False
        self.fuel = 10
        self.last_fuel_update_time = time.time()
        self.max_hp = 5 + playerstatus.status.getfighterHPUpgrade() * 2
        self.hp = 5 + playerstatus.status.getfighterHPUpgrade() * 2
        if Fighter.gauge is None:
            Fighter.gauge = gfw.Gauge('resources/gauge_fg.png', 'resources/gauge_bg.png')

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Fighter.KEY_MAP:
            if e.key == SDLK_a or e.key == SDLK_d:
                self.dx += Fighter.KEY_MAP[pair]
            elif e.key == SDLK_w or e.key == SDLK_s:
                self.dy += Fighter.KEY_MAP[pair]
            # elif e.key == SDLK_SPACE:
            #     self.shot = Fighter.KEY_MAP[pair]

    def update(self):
        if self.operating == True:
            self.x += self.dx * self.speed * gfw.frame_time
            self.y += self.dy * self.speed * gfw.frame_time
            self.x = clamp(self.min_x, self.x, self.max_x)
            self.y = clamp(self.min_y, self.y, self.max_y)
            self.laser_time += gfw.frame_time
            if self.laser_time >= Fighter.LASER_INTERVAL:
                self.fire()
            self.update_roll()
            current_time = time.time()
            if current_time - self.last_fuel_update_time >= 1:  # 1초 경과 확인
                self.fuel -= 1  # 연료 소모
                self.last_fuel_update_time = current_time  # 시간 갱신
            if self.fuel <= 0:
                self.operating = False


    def update_roll(self):
        roll_dir = self.dx
        if roll_dir == 0: # 현재 비행기가 움직이고 있지 않은데
            if self.roll_time > 0:   # roll 이 + 라면
                roll_dir = -1        #  감소시킨다
            elif self.roll_time < 0: # roll 이 - 라면
                roll_dir = 1         #  증가시킨다

        self.roll_time += roll_dir * gfw.frame_time
        self.roll_time = clamp(-Fighter.MAX_ROLL, self.roll_time, Fighter.MAX_ROLL)

        if self.dx == 0: # 현재 비행기가 움직이고 있지 않은데
            if roll_dir < 0 and self.roll_time < 0: # roll 이 감소중이었고 0 을 지나쳤으면
                self.roll_time = 0                  # 0 이 되게 한다
            if roll_dir > 0 and self.roll_time > 0: # roll 이 증가중이었고 0 을 지나쳤으면
                self.roll_time = 0                  # 0 이 되게 한다

        roll = int(self.roll_time * 5 / Fighter.MAX_ROLL)
        self.src_rect = Fighter.IMAGE_RECTS[roll + 5] # [-5 ~ +5] 를 [0 ~ 10] 으로 변환한다.
    def draw(self):
        # super().draw()
        if self.operating == True:
            self.image.clip_draw(*self.src_rect, self.x, self.y)
            if self.laser_time < Fighter.SPARK_INTERVAL:
                self.spark_image.draw(self.x, self.y + Fighter.SPARK_OFFSET)
            gy = self.y - self.WIDTH // 2
            rate = self.hp / self.max_hp
            self.gauge.draw(self.x, gy, self.WIDTH - 10, rate)

    def fire(self):
        self.laser_time = 0
        world = gfw.top().world
        world.append(Bullet(self.x, self.y), world.layer.bullet)
        game_scene.beamSound()

    def get_bb(self):
        return self.x - 30, self.y - 32, self.x + 30, self.y + 28

    def dead(self):
        self.hp -= 1
        return self.hp <= 0
class Bullet(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/laser_1.png', x, y)
        self.speed = 400 # 400 pixels per second
        self.max_y = get_canvas_height() + self.image.h
        self.power = 40 + playerstatus.status.getfighterATKUpgrade() * 20
        self.layer_index = gfw.top().world.layer.bullet
    def update(self):
        self.y += self.speed * gfw.frame_time
        if self.y > self.max_y:
            gfw.top().world.remove(self)
