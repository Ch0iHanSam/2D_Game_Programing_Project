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
        if self.judge_click == True:
            self.image.draw(750, 50)


    def draw(self):
        if self.image != None:
            self.image.draw(self.x, self.y)
            self.equip()


    def attack(self, Player):
        if self.judge_click == True:
            print(Player.damage,'만큼의 피해를 입혔습니다!')
            self.judge_attack = True


    def Shield_ability(self):
        if self.judge_click == True:
            if self.name == '../Object/Shield/Shield_BlueShield.png':
                pass #스텟 조정이기 때문에 Handle_Event 부분에 구현해놓음
            elif self.name == '../Object/Shield/Shield_RedCrossShield.png':
                    if self.judge_attack == True:
                        print('HP를 5만큼 회복했습니다!')
        if self.judge_attack == True:
            self.judge_attack = False