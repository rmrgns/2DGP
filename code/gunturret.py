from pico2d import *
import gfw

import game_scene
import playerstatus

class GunTurret(gfw.Sprite):
    LASER_INTERVAL = 0.5
    SPARK_INTERVAL = 0.05
    SPARK_OFFSET = 28
    def __init__(self, x, y):
        super().__init__('resources/attack.png', x, y)
        self.x, self.y = x,y
        self.width , self.height = self.image.w, self.image.h
        self.hp = 1
        self.laser_time = 0
        self.spark_image = gfw.image.load('resources/laser_0.png')
        self.shot = 0
        self.turret_type = 1

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            #print(self.width, "+", self.height)
            x, y = e.x, get_canvas_height() - e.y
            if self.is_clicked(x, y):  # 클릭된 빈 공간이나 터렛 확인
                if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                    if self.turret_type == 1:  # 1번 터렛이면 빈 공간으로 변경
                        self.to_empty_space()


    def update(self):
        self.laser_time += gfw.frame_time
        if self.laser_time >= GunTurret.LASER_INTERVAL:
            self.fire()
            game_scene.beamSound()
        pass

    def draw(self):
        self.image.draw(self.x, self.y,50,50)
        if self.laser_time < GunTurret.SPARK_INTERVAL:
            self.spark_image.draw(self.x, self.y + GunTurret.SPARK_OFFSET)
        pass

    def is_clicked(self, x, y):
        left, bottom, right, top = self.get_bb()
        return left <= x <= right and bottom <= y <= top

    def get_bb(self):
        half_width = self.width // 2
        half_height = self.height // 2
        return (self.x - half_width, self.y - half_height,
                self.x + half_width, self.y + half_height)
    def fire(self):
        if playerstatus.status.bRound:
            self.laser_time = 0
            world = gfw.top().world
            new_bullet = Bullet(self.x,self.y)
            world.append(new_bullet, world.layer.bullet)

    def to_empty_space(self):
        newturret = game_scene.Turret(self.x, self.y)  # 빈 공간 생성
        game_scene.world.append(newturret, game_scene.world.layer.turret)
        game_scene.world.remove(self, game_scene.world.layer.turret)  # 기존 터렛 삭제

    def dead(self, power):
        self.hp -= power
        return self.hp <= 0

class Bullet(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/laser_1.png', x, y)
        self.speed = 400 # 400 pixels per second
        self.max_y = get_canvas_height() + self.image.h
        self.power = 40 + playerstatus.status.getgunturretATKUpgrade() * 20
        self.layer_index = gfw.top().world.layer.bullet
    def update(self):
        self.y += self.speed * gfw.frame_time
        if self.y > self.max_y:
            gfw.top().world.remove(self)
