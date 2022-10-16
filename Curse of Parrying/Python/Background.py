from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('../BackGround/Practice.png')
        self.x, self.y = 400, 300

    def draw(self):
        self.image.draw(self.x, self.y)

