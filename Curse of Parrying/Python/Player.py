from pico2d import *

#걷기
class Player:
    def __init__(self):
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 'idle'
        self.exdir = 'right'
        self.dash = 'off'
        self.parrying = 'off'
        self.damage = 10

    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'up':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'down':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.dir == 'right':
            self.x += 5
        elif self.dir == 'left':
            self.x -= 5
        elif self.dir == 'up':
            self.y += 5
        elif self.dir == 'down':
            self.y -= 5

    def set_exdir(self):
        if self.dir == 'right' or self.dir == 'left':
            self.exdir = self.dir

#대쉬
class Player_Dash:
    def __init__(self):
        self.image = load_image('../Object/Character/Dash/Character_Player_Dash.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir = ' '
        self.exdir = ' '

    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'up':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'down':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def set_dir(self, Player):
        self.dir = Player.dir
        self.exdir = Player.exdir
        self.x = Player.x
        self.y = Player.y

    def update(self, Player):
        self.frame = (self.frame + 1) % 4
        if self.dir == 'right':
            self.x += 15
            Player.x = self.x
        elif self.dir == 'left':
            self.x -= 15
            Player.x = self.x
        elif self.dir == 'up':
            self.y += 15
            Player.y = self.y
        elif self.dir == 'down':
            self.y -= 15
            Player.y = self.y
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.x += 15
                Player.x = self.x
            elif self.exdir == 'left':
                self.x -= 15
                Player.x = self.x

#패링
class Player_Parrying:
    def __init__(self):
        self.image = load_image('../Object/Character/Parrying/Character_Player_Parrying.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.exdir = ' '
        self.shieldNone = True

    def draw(self):
        if self.exdir == 'right':
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.exdir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 9

    def set_exdir(self, Player):
        self.exdir = Player.exdir
        self.x, self.y = Player.x, Player.y

    def hit(self, Effects, Shield_Use_1, Shield_Use_2, Shields, Player_):
        for effect in Effects:
            if self.x-60 < effect.x < self.x+60 and self.y-60 < effect.y < self.y+60:
                Effects.remove(effect)
                Shield_Use_1()
                Shield_Use_2()
                for shield in Shields:
                    if shield.judge_click:
                        self.shieldNone = False
                if self.shieldNone:
                    print(Player_.damage, '만큼의 피해를 입혔습니다!')

