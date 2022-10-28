from pico2d import *


# 몬스터박스 클래스
class MonsterBox:
    def __init__(self):
        self.image = load_image('../Object/ETC/MonsterBox.png')
        self.x, self.y = 600, 500

    def draw(self):
        self.image.draw(self.x, self.y)


# 몬스터박스2 클래스
class MonsterBox2:
    def __init__(self):
        self.image = load_image('../Object/ETC/MonsterBox2.png')
        self.x, self.y = 500, 500

    def draw(self):
        self.image.draw(self.x, self.y)