from pico2d import *
import gfw
import game_scene

class CmdCenter(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/center.png', x, y)
        self.x, self.y = x,y
        self.width, self.height = self.image.w, self.image.h
        self.hp = 1


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        half_width = self.width // 2
        half_height = self.height // 2
        return (self.x - half_width, self.y - half_height,
                self.x + half_width, self.y + half_height)

    def dead(self, power):
        self.hp -= power
        return self.hp <= 0