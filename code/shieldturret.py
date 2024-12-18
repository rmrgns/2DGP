from pico2d import *
import gfw

import game_scene
import playerstatus

class ShieldTurret(gfw.Sprite):
    WIDTH = 100
    gauge = None

    def __init__(self, x, y):
        super().__init__('resources/shield.png', x, y)
        self.x, self.y = x,y
        self.width, self.height = self.image.w, self.image.h

        self.hp = 10 + playerstatus.status.getshieldturretHPUpgrade() * 2
        self.max_hp = 10 + playerstatus.status.getshieldturretHPUpgrade() * 2
        self.turret_type = 2

        if ShieldTurret.gauge is None:
            ShieldTurret.gauge = gfw.Gauge('resources/gauge_fg.png', 'resources/gauge_bg.png')

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            x, y = e.x, get_canvas_height() - e.y
            if self.is_clicked(x, y):  # 클릭된 빈 공간이나 터렛 확인
                if e.button == SDL_BUTTON_RIGHT:  # 우클릭
                    if self.turret_type == 2:  # 2번 터렛이면 빈 공간으로 변경
                        self.to_empty_space()


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y,50,50)
        gy = self.y - self.WIDTH // 2
        rate = self.hp / self.max_hp
        self.gauge.draw(self.x, gy, self.WIDTH - 10, rate)


    def is_clicked(self, x, y):
        left, bottom, right, top = self.get_bb()
        return left <= x <= right and bottom <= y <= top

    def get_bb(self):
        half_width = self.width // 2
        half_height = self.height // 2
        return (self.x - half_width, self.y - half_height,
                self.x + half_width, self.y + half_height)

    def to_empty_space(self):
        newturret = game_scene.Turret(self.x, self.y)  # 빈 공간 생성
        game_scene.world.append(newturret, game_scene.world.layer.turret)
        game_scene.world.remove(self, game_scene.world.layer.turret)

    def dead(self, power):
        self.hp -= power
        return self.hp <= 0