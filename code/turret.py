from pico2d import *
import gfw
from gunturret import GunTurret
from shieldturret import ShieldTurret
import game_scene
import playerstatus

class Turret(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/build.png', x, y)
        self.x, self.y = x,y
        self.width, self.height = self.image.w, self.image.h
        self.turret_type = 0

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            x, y = e.x, get_canvas_height() - e.y
            if self.is_clicked(x, y):  # 클릭된 빈 공간이나 터렛 확인
                if playerstatus.status.gold < 200:
                    return
                if e.button == SDL_BUTTON_LEFT:  # 좌클릭
                    if self.turret_type == 0:  # 빈 공간이면 1번 터렛 설치
                        self.build_GunTurret()
                elif e.button == SDL_BUTTON_RIGHT:  # 우클릭
                    if self.turret_type == 0:  # 빈 공간이면 2번 터렛 설치
                        self.build_ShieldTurret()
                playerstatus.status.gold -= 200
                game_scene.getGold_scoreBtn().score = playerstatus.status.gold


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

    def build_ShieldTurret(self):
        shield = ShieldTurret(self.x, self.y)
        game_scene.world.append(shield, game_scene.world.layer.turret)
        game_scene.world.remove(self, game_scene.world.layer.turret)

    def to_empty_space(self):
        newturret = Turret(self.x, self.y)  # 빈 공간 생성
        game_scene.world.append(newturret, game_scene.world.layer.turret)
        game_scene.world.remove(self, game_scene.world.layer.turret)  # 기존 터렛 삭제
