from pico2d import *


# 걷기
class Player:
    def __init__(self):
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.exdir = 1
        self.damage = 10
        self.delay = 0
        self.hp = 100

    def draw(self):
        if self.dir_x > 0:  # 오른쪽
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir_x < 0:  # 왼쪽
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_y > 0:  # 위
            if self.exdir > 0:  # 오른쪽 바라봄
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir < 0:  # 왼쪽 바라봄
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_y < 0:  # 아래
            if self.exdir < 0:  # 오른쪽 바라봄
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir > 0:  # 왼쪽 바라봄
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_x == 0:  # 정지
            if self.exdir > 0:  # 오른쪽 바라봄
                self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir < 0:  # 왼쪽 바라봄
                self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 5 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * 2.5
        self.y += self.dir_y * 2.5

    def set_exdir(self):
        if self.dir_x > 0 or self.dir_x < 0:
            self.exdir = self.dir_x

    def check_hit(self, Effects):
        for i in range(len(Effects)):
            if self.x - 30 < Effects[i].x < self.x + 30 and self.y - 30 < Effects[i].y < self.y + 30:
                Effects[i].judge = False
                self.hp -= 30
                print(self.hp)
        if self.hp <= 0:
            self.x, self.y = 400, 90
            self.hp = 100


# 패링
class Player_Parrying:
    def __init__(self):
        self.image = load_image('../Object/Character/Parrying/Character_Player_Parrying.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.exdir = 0
        self.delay = 0
        self.do = False

    def draw(self):
        if self.exdir > 0:
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.exdir < 0:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 2 == 0:
            if self.frame == 8:
                self.do = False
            self.frame = (self.frame + 1) % 9

    def set_exdir(self, Player):
        self.exdir = Player.exdir
        self.x, self.y = Player.x, Player.y

    def hit(self, Effects, Shield_Use_1, Shield_Use_2, Player):
        for effect in Effects:
            if self.x - 30 < effect.x < self.x + 30 and self.y - 30 < effect.y < self.y + 30:
                Effects.remove(effect)
                Shield_Use_1()
                Shield_Use_2()
                effect.monster.hp -= Player.damage
