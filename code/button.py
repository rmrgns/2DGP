from pico2d import *
import gfw

class Button(gfw.Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.x, self.y = x,y
        self.width, self.height = self.image.w, self.image.h

    def handle_event(self, e):
        pass

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