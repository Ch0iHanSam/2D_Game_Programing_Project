from pico2d import *


# 상호작용 클래스
class Interact:
    def __init__(self):
        self.image = load_image('../Effect/ETC/interact.png')
        self.x, self.y = 0, 0
        self.judge = 'off'

    def draw(self, Object, bndry):
        if (Object.x + bndry > self.x > Object.x - bndry) and (Object.y + bndry > self.y > Object.y - bndry):
            self.judge = 'on'
            self.image.draw(self.x, self.y)
        else:
            self.judge = 'off'

    def set_xy(self, Player):
        self.x, self.y = Player.x, Player.y
