from pico2d import *

class Test_Monster_Effect:
    def __init__(self, x = 0, y = 0):
        self.x, self.y, self.frame, self.delay = x, y, 0, 0
        self.image = load_image('../Object/Enemy/Test/Effect.png')
        self.first = True
        self.damage = 5
        self.monster = None

    def draw(self):
        self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 4 == 0:
            self.frame = (self.frame + 1) % 4
        self.x += 1  # 이건 속도 리팩토리 할 때 고쳐야함

    def set_xy(self, monster):
        if self.first:
            self.x = monster.x + 30
            self.y = monster.y
            self.monster = monster
            self.first = False


class Lego:  # 미완 - 장난감 방패에 들어갈 것임
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.damage = 3
        self.image = load_image('../Effect/Character/Lego.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def check_hit(self, Target):
        if self.x - 10 < Target.x < self.x + 10 and self.y < Target.y < self.y + 20:
            Target.HP -= self.damage

#인터페이스
#HP
class HP:
    def __init__(self, Player):
        if Player.HP == 100:
            self.image = load_image('../Effect/Character/HP/HP=100.png')
        elif Player.HP == 95:
            self.image = load_image('../Effect/Character/HP/HP=95.png')
        elif Player.HP == 90:
            self.image = load_image('../Effect/Character/HP/HP=90.png')
        elif Player.HP == 85:
            self.image = load_image('../Effect/Character/HP/HP=85.png')
        elif Player.HP == 80:
            self.image = load_image('../Effect/Character/HP/HP=80.png')
        elif Player.HP == 75:
            self.image = load_image('../Effect/Character/HP/HP=75.png')
        elif Player.HP == 70:
            self.image = load_image('../Effect/Character/HP/HP=70.png')
        elif Player.HP == 65:
            self.image = load_image('../Effect/Character/HP/HP=65.png')
        elif Player.HP == 60:
            self.image = load_image('../Effect/Character/HP/HP=60.png')
        elif Player.HP == 55:
            self.image = load_image('../Effect/Character/HP/HP=55.png')
        elif Player.HP == 50:
            self.image = load_image('../Effect/Character/HP/HP=50.png')
        elif Player.HP == 45:
            self.image = load_image('../Effect/Character/HP/HP=45.png')
        elif Player.HP == 40:
            self.image = load_image('../Effect/Character/HP/HP=40.png')
        elif Player.HP == 35:
            self.image = load_image('../Effect/Character/HP/HP=35.png')
        elif Player.HP == 30:
            self.image = load_image('../Effect/Character/HP/HP=30.png')
        elif Player.HP == 25:
            self.image = load_image('../Effect/Character/HP/HP=25.png')
        elif Player.HP == 20:
            self.image = load_image('../Effect/Character/HP/HP=20.png')
        elif Player.HP == 15:
            self.image = load_image('../Effect/Character/HP/HP=15.png')
        elif Player.HP == 10:
            self.image = load_image('../Effect/Character/HP/HP=10.png')
        elif Player.HP == 5:
            self.image = load_image('../Effect/Character/HP/HP=5.png')
        self.x = 110
        self.y = 490

    def update(self, Player):
        if Player.HP == 100:
            self.image = load_image('../Effect/Character/HP/HP=100.png')
        elif Player.HP == 95:
            self.image = load_image('../Effect/Character/HP/HP=95.png')
        elif Player.HP == 90:
            self.image = load_image('../Effect/Character/HP/HP=90.png')
        elif Player.HP == 85:
            self.image = load_image('../Effect/Character/HP/HP=85.png')
        elif Player.HP == 80:
            self.image = load_image('../Effect/Character/HP/HP=80.png')
        elif Player.HP == 75:
            self.image = load_image('../Effect/Character/HP/HP=75.png')
        elif Player.HP == 70:
            self.image = load_image('../Effect/Character/HP/HP=70.png')
        elif Player.HP == 65:
            self.image = load_image('../Effect/Character/HP/HP=65.png')
        elif Player.HP == 60:
            self.image = load_image('../Effect/Character/HP/HP=60.png')
        elif Player.HP == 55:
            self.image = load_image('../Effect/Character/HP/HP=55.png')
        elif Player.HP == 50:
            self.image = load_image('../Effect/Character/HP/HP=50.png')
        elif Player.HP == 45:
            self.image = load_image('../Effect/Character/HP/HP=45.png')
        elif Player.HP == 40:
            self.image = load_image('../Effect/Character/HP/HP=40.png')
        elif Player.HP == 35:
            self.image = load_image('../Effect/Character/HP/HP=35.png')
        elif Player.HP == 30:
            self.image = load_image('../Effect/Character/HP/HP=30.png')
        elif Player.HP == 25:
            self.image = load_image('../Effect/Character/HP/HP=25.png')
        elif Player.HP == 20:
            self.image = load_image('../Effect/Character/HP/HP=20.png')
        elif Player.HP == 15:
            self.image = load_image('../Effect/Character/HP/HP=15.png')
        elif Player.HP == 10:
            self.image = load_image('../Effect/Character/HP/HP=10.png')
        elif Player.HP == 5:
            self.image = load_image('../Effect/Character/HP/HP=5.png')

    def draw(self):
        self.image.draw(self.x, self.y, 200, 200)

#일시정지
class Pause:
    def __init__(self):
        self.x, self.y = 770, 570
        self.image = load_image('../BackGround/Pause_Mark.png')

    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)