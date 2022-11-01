from pico2d import *


class Shield:
    def __init__(self):
        self.image = None
        self.name = None
        self.x, self.y = 750, 50
        self.judge_attack = False
        self.judge_click = False

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def set_Shield(self, name):
        self.name = str(name)
        self.image = load_image(name)

    def equip(self):
        if self.judge_click:
            self.image.draw(750, 50)

    def draw(self):
        if self.image is not None:
            self.image.draw(self.x, self.y)
            self.equip()

    def attack(self):
        if self.judge_click:
            self.judge_attack = True

    def Shield_ability(self, Player):
        if self.judge_click:
            if self.name == '../Object/Shield/Shield_BlueShield.png':
                pass  # 스텟 조정이기 때문에 Handle_Event 부분에 구현해놓음
            elif self.name == '../Object/Shield/Shield_RedCrossShield.png':
                if self.judge_attack:
                    Player.hp += 10
                    print(Player.hp)
        if self.judge_attack:
            self.judge_attack = False
