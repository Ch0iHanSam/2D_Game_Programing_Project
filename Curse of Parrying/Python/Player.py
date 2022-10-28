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
        self.dash = False
        self.parrying = 'off'
        self.damage = 10
        self.delay = 0

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
        if self.delay % 3 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5

    def set_exdir(self):
        if self.dir_x > 0 or self.dir_x < 0:
            self.exdir = self.dir_x


# 대쉬
class Player_Dash:
    def __init__(self):
        self.image = load_image('../Object/Character/Dash/Character_Player_Dash.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir_x = 0
        self.dir_y = 0
        self.exdir = 0

    def draw(self):
        if self.dir_x > 0:
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir_x < 0:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_y > 0:
            if self.exdir > 0:
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir < 0:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_y < 0:
            if self.exdir > 0:
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir < 0:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def set_dir(self, Player):
        if Player.dir_x != 0 or Player.dir_y != 0:
            self.dir_x = Player.dir_x
            self.dir_y = Player.dir_y
            self.exdir = Player.exdir
            self.x = Player.x
            self.y = Player.y

    def update(self, Player):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir_x * 15
        Player.x = self.x
        self.y += self.dir_y * 15
        Player.y = self.y


# 패링
class Player_Parrying:
    def __init__(self):
        self.image = load_image('../Object/Character/Parrying/Character_Player_Parrying.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.exdir = 0
        self.shieldNone = True

    def draw(self):
        if self.exdir > 0:
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.exdir < 0:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 9

    def set_exdir(self, Player):
        self.exdir = Player.exdir
        self.x, self.y = Player.x, Player.y

    def hit(self, Effects, Shield_Use_1, Shield_Use_2, Shields, Player_):
        for effect in Effects:
            if self.x - 30 < effect.x < self.x + 30 and self.y - 30 < effect.y < self.y + 30:
                Effects.remove(effect)
                Shield_Use_1()
                Shield_Use_2()
                for shield in Shields:
                    if shield.judge_click:
                        self.shieldNone = False
                if self.shieldNone:
                    print(Player_.damage, '만큼의 피해를 입혔습니다!')