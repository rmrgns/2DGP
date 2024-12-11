from pico2d import *
import random
import gfw

import game_scene
class Enemy(gfw.AnimSprite):
    LASER_INTERVAL = 2
    WIDTH = 100
    MAX_LEVEL = 20
    gauge = None

    def __init__(self, index, level, enemy_type):
        x = self.WIDTH * index + self.WIDTH // 2
        y = get_canvas_height() + self.WIDTH // 2
        self.level = level
        self.enemy_type = enemy_type
        self.elapsed_time = 0  # 적3의 행동 시간 추적
        self.fired = False     # 적3 공격 여부
        super().__init__(f'resources/monster_{enemy_type}.png', x, y, 10)
        self.speed = -100 if enemy_type != 3 else -50
        self.max_life = level * 100
        self.life = self.max_life
        self.score = self.max_life
        self.laser_time = 0
        if Enemy.gauge is None:
            Enemy.gauge = gfw.Gauge('res/gauge_fg.png', 'res/gauge_bg.png')
        self.layer_index = gfw.top().world.layer.enemy

    def update(self):
        self.elapsed_time += gfw.frame_time
        if self.enemy_type == 3:
            if self.elapsed_time <= 4.0:  # 1초간 이동
                self.y += self.speed * gfw.frame_time
            elif not self.fired:  # 멈추고 공격
                self.fired = True
            self.laser_time += gfw.frame_time
            if self.laser_time >= Enemy.LASER_INTERVAL:
                self.fire()
        else:
            self.y += self.speed * gfw.frame_time

        if self.y < -self.WIDTH:
            gfw.top().world.remove(self)

    def fire(self):
        # 적3의 반대 방향 발사체
        self.laser_time = 0
        world = gfw.top().world
        bullet = Bullet(self.x, self.y)
        gfw.top().world.append(bullet, world.layer.enemybullet)

    def draw(self):
        super().draw()
        gy = self.y - self.WIDTH // 2
        rate = self.life / self.max_life
        self.gauge.draw(self.x, gy, self.WIDTH - 10, rate)

    def decrease_life(self, power):
        self.life -= power
        return self.life <= 0

    def get_bb(self):
        r = 42
        return self.x - r, self.y - r, self.x + r, self.y + r


class EnemyGen:
    GEN_INTERVAL = 5.0
    GEN_INIT = 1.0
    GEN_X = [50, 150, 250, 350, 450]

    def __init__(self):
        self.time = self.GEN_INTERVAL - self.GEN_INIT
        self.wave_index = 0

    def draw(self):
        pass

    def update(self):
        self.time += gfw.frame_time
        if self.time < self.GEN_INTERVAL:
            return

        for i in range(5):
            # 적의 종류를 확률적으로 결정
            rand = random.random() * 100
            if rand < 50:
                enemy_type = 1
            elif rand < 90:
                enemy_type = 2
            else:
                enemy_type = 3

            # 적 생성 및 추가
            level = clamp(1, (self.wave_index + 18) // 10, Enemy.MAX_LEVEL)
            gfw.top().world.append(Enemy(i, level, enemy_type))

        self.time -= self.GEN_INTERVAL
        self.wave_index += 1


class Bullet(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/monsterlaser.png', x, y)
        self.speed = -400 # 400 pixels per second
        self.max_y = get_canvas_height() + self.image.h
        self.power = 1
        self.layer_index = gfw.top().world.layer.enemybullet
    def update(self):
        self.y += self.speed * gfw.frame_time
        if self.y > self.max_y:
            gfw.top().world.remove(self)