from pico2d import *


class MonsterBox:
    def __init__(self):
        self.image = load_image('../Object/ETC/MonsterBox.png')
        self.x, self.y = 700, 500

    def draw(self):
        self.image.draw(self.x, self.y)