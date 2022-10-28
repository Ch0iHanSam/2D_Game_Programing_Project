from pico2d import *


# 몬스터 클래스
class Test_Monster:
    def __init__(self):
        self.image = load_image('../Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Attack.png')
        self.x, self.y = 100, 200
        self.frame = 0
        self.summon = 'off'
        self.delay = 0

    def draw(self):
        if self.summon == 'on':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.summon == 'on':
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
        self.judge = 'off'
        self.delay = 0

    def draw(self):
        if self.judge == 'on':
            if self.x < 700:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.judge == 'on':
            self.delay += 1
            if self.delay > 100:
                self.delay = 0
            if self.delay%4 == 0:
                self.frame = (self.frame + 1) % 7
            self.x += 2
        if self.x > 700:
            self.judge = 'off'
