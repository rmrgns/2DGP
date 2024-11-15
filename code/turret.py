from pico2d import *
import gfw
from gunturret import GunTurret
import game_scene

class Turret(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/build.png', x, y)
        self.x, self.y = x,y
        self.width, self.height = self.image.w, self.image.h
        self.turret_type = 0
    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            x, y = e.x, get_canvas_height() - e.y  # y 좌표 반전
            if self.is_clicked(x, y):
                # 클릭시 터렛 설치
                self.build_GunTurret()


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

        pass

    def is_clicked(self, x, y):
        left, bottom, right, top = self.get_bb()
        return left <= x <= right and bottom <= y <= top

    def get_bb(self):
        half_width = self.width // 2
        half_height = self.height // 2
        return (self.x - half_width, self.y - half_height,
                self.x + half_width, self.y + half_height)

    def build_GunTurret(self):
        gun = GunTurret(self.x, self.y)
        game_scene.world.append(gun, game_scene.world.layer.turret)
        game_scene.world.remove(self, game_scene.world.layer.turret)
        pass