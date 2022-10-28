from pico2d import *
import random

# 테스트 몬스터 클래스
class Test_Monster:
    def __init__(self):
        self.image = load_image('../Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Attack.png')
        self.x, self.y = 100, 200
        self.frame = 0
        self.summon = False
        self.delay = 0

    def draw(self):
        if self.summon:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.summon:
            self.delay += 1
            if self.delay > 100:
                self.delay = 0
            if self.delay % 4 == 0:
                self.frame = (self.frame + 1) % 9


# 테스트용 몬스터의 공격 이펙트 클래스
class Test_Monster_Attack_Effect:
    def __init__(self):
        self.image = load_image('../Effect/Monster/Monster_Attack/Pigeon/Pigeon_Attack.png')
        self.x, self.y = 100, 200
        self.frame = 0
        self.judge = False
        self.delay = 0

    def draw(self):
        if self.judge:
            if self.x < 700:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.judge:
            self.delay += 1
            if self.delay > 100:
                self.delay = 0
            if self.delay%4 == 0:
                self.frame = (self.frame + 1) % 7
            self.x += 2
        if self.x > 700:
            self.judge = False


# 스테이지1 몬스터(멧돼지) 클래스
class Boar:
    def __init__(self):
        self.image = load_image('../Object/Enemy/Stage1/Boar/Enemy_Boar_Move.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.summon = False
        self.delay = 0

    def draw(self):
        self.image.clip_draw(0*self.frame, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.summon == True:
            if self.summon:
                self.delay += 1
                if self.delay > 100:
                    self.delay = 0
                if self.delay % 4 == 0:
                    self.frame = (self.frame + 1) % 6

    def set_xy(self):
        self.x = random.randint(100, 701)
        self.y = random.randint(100, 501)


# 스테이지1 몬스터(토끼) 클래스
class Rabbit:
    def __init__(self):
        self.image = load_image('../Object/Enemy/Stage1/Rabbit/Enemey_Rabbit_Move.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.summon = False
        self.delay = 0

    def draw(self):
        self.image.clip_draw(0 * self.frame, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.summon == True:
            if self.summon:
                self.delay += 1
                if self.delay > 100:
                    self.delay = 0
                if self.delay % 4 == 0:
                    self.frame = (self.frame + 1) % 7

    def set_xy(self):
        self.x = random.randint(100, 701)
        self.y = random.randint(100, 501)


# 스테이지1 몬스터(비둘기) 클래스
class Pigeon:
    def __init__(self):
        self.image = load_image('../Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Fly.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.summon = False
        self.delay = 0

    def draw(self):
        self.image.clip_draw(68 * self.frame, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.summon == True:
            if self.summon:
                self.delay += 1
                if self.delay > 100:
                    self.delay = 0
                if self.delay % 4 == 0:
                    self.frame = (self.frame + 1) % 7

    def set_xy(self):
        self.x = random.randint(100, 701)
        self.y = random.randint(100, 501)


# 소환 마법진 클래스
class Summon:
    def __init__(self):
        self.image = load_image('../Effect/Monster/Effect_Summon.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.delay = 0

    def draw(self):
        self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 4 == 0:
            self.frame = (self.frame + 1) % 17

    def set_xy(self, monster):
        monster.x = self.x
        monster.y = self.y