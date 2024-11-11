from pico2d import *
import gfw

class Turret(gfw.Sprite):
    def __init__(self, x, y):
        super().__init__('resources/build.png', x, y)
        self.x, self.y = x,y

    def handle_event(self, e):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw_to_origin(self.x, self.y, 10, 10)

        pass
    def get_bb(self):
        r = 42
        return self.x - r, self.y - r, self.x + r, self.y + r