from pico2d import *
import gfw
import game_scene

class CmdCenter(gfw.Sprite):
    def __init__(self, x, y, hp=1):
        super().__init__('resources/center.png', x, y)
        self.x, self.y = x,y
        self.width, self.height = self.image.w, self.image.h
        self.hp = hp


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

        pass
