from pico2d import *
import game_framework
import random

class Test_Monster:
    def __init__(self, x = 200, y = 100):
        self.x, self.y, self.frame = x, y, 0
        self.image = load_image('../Object/Enemy/Test/Enemy_Test_Attack.png')
        self.summon = False
        self.delay = 0
        self.attack = False
        self.val_check_attack = 0  # 어택 변환 용으로 사용됨. 다른 곳에 사용되지 않음
        self.HP = 30

    def draw(self):
        if self.summon:
            self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.HP <= 0:
            self.summon = False
            self.HP = 30
        if self.summon:
            self.delay += 1
            if self.delay == 100:
                self.delay = 0
            if self.delay%6 == 0:
                self.frame = (self.frame+1)%10
            self.val_check_attack += 1
            if self.val_check_attack == 31:
                self.attack = True  # 최초 5프레임 달성 시에만 (1 증가시키고 나서니까 화면 상에서는 5, 코드 상에선 6)소환 시키게끔 / 6*5=30
            else:
                if self.attack:
                    self.attack = False
            if self.frame == 0:
                self.val_check_attack = 0

    def set_summon(self):
        if self.summon:
            self.summon = False
            self.frame = 0
        else:
            self.summon = True

class Test_Monster_Effect:
    def __init__(self, x = 0, y = 0):
        self.x, self.y, self.frame, self.delay = x, y, 0, 0
        self.image = load_image('../Object/Enemy/Test/Effect.png')
        self.first = True
        self.damage = 20
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



#
# # 변수 모음 클래스
# class Variable:
#     def __init__(self):
#         self.monster_judge = False
#         self.magic_circle_summon_judge = False
#         self.monster_summon = False
#
#
# # 테스트 몬스터 클래스
# class Test_Monster:
#     def __init__(self):
#         self.image = load_image('../Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Attack.png')
#         self.x, self.y = 100, 200
#         self.frame = 0
#         self.summon = False
#         self.delay = 0
#         self.hp = 30
#
#     def draw(self):
#         if self.summon:
#             self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
#
#     def update(self):
#         if self.summon:
#             self.delay += 1
#             if self.delay > 100:
#                 self.delay = 0
#             if self.delay % 4 == 0:
#                 self.frame = (self.frame + 1) % 9
#         if self.hp <= 0:
#             print('테스트 몬스터가 처치되었습니다')
#             self.summon = False
#             self.hp = 30 #이후 몬스터를 리스트로 관리할 것이기 때문에 hp를 원래대로 돌려줄 필요는 없음
#
#
# # 테스트용 몬스터의 공격 이펙트 클래스
# class Test_Monster_Attack_Effect:
#     def __init__(self, Monster):
#         self.image = load_image('../Effect/Monster/Monster_Attack/Pigeon/Pigeon_Attack.png')
#         self.x, self.y = 100, 200
#         self.frame = 0
#         self.judge = False
#         self.delay = 0
#         self.monster = Monster
#
#     def draw(self):
#         if self.judge:
#             if self.x < 700:
#                 self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
#
#     def update(self, List):
#         if self.judge:
#             self.delay += 1
#             if self.delay > 100:
#                 self.delay = 0
#             if self.delay % 4 == 0:
#                 self.frame = (self.frame + 1) % 7
#             self.x += 2
#         if self.x > 700:
#             List.remove(self)
#
#     def check_pop(self, List):
#         if not self.judge:
#             List.remove(self)
#
#
# # 스테이지1 몬스터(멧돼지) 클래스
# class Boar:
#     def __init__(self):
#         self.image = load_image('../Object/Enemy/Stage1/Boar/Enemy_Boar_Move.png')
#         self.x, self.y = 0, 0
#         self.frame = 0
#         self.delay = 0
#         self.hp = 50
#
#     def draw(self):
#         self.image.clip_draw(68*self.frame, 0, 68, 68, self.x, self.y)
#
#     def update(self):
#         self.delay += 1
#         if self.delay > 100:
#             self.delay = 0
#         if self.delay % 4 == 0:
#             self.frame = (self.frame + 1) % 6
#
#     def set_xy(self):
#         self.x = random.randint(100, 701)
#         self.y = random.randint(100, 501)
#
#
# # 스테이지1 몬스터(토끼) 클래스
# class Rabbit:
#     def __init__(self):
#         self.image = load_image('../Object/Enemy/Stage1/Rabbit/Enemey_Rabbit_Move.png')
#         self.x, self.y = 0, 0
#         self.frame = 0
#         self.delay = 0
#         self.hp = 30
#
#     def draw(self):
#         self.image.clip_draw(68 * self.frame, 0, 68, 68, self.x, self.y)
#
#     def update(self):
#         self.delay += 1
#         if self.delay > 100:
#             self.delay = 0
#         if self.delay % 4 == 0:
#             self.frame = (self.frame + 1) % 7
#
#     def set_xy(self):
#         self.x = random.randint(100, 701)
#         self.y = random.randint(100, 501)
#
#
# # 스테이지1 몬스터(비둘기) 클래스
# class Pigeon:
#     def __init__(self):
#         self.image = load_image('../Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Fly.png')
#         self.x, self.y = 0, 0
#         self.frame = 0
#         self.delay = 0
#         self.hp = 0
#
#     def draw(self):
#         self.image.clip_draw(68 * self.frame, 0, 68, 68, self.x, self.y)
#
#     def update(self):
#         self.delay += 1
#         if self.delay > 100:
#             self.delay = 0
#         if self.delay % 4 == 0:
#             self.frame = (self.frame + 1) % 7
#
#     def set_xy(self):
#         self.x = random.randint(100, 701)
#         self.y = random.randint(100, 501)
#
#
# # 소환 마법진 클래스
# class Summon:
#     def __init__(self):
#         self.image = load_image('../Effect/Monster/Effect_Summon.png')
#         self.x, self.y = 0, 0
#         self.frame = 0
#         self.delay = 0
#
#     def draw(self):
#         self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)
#
#     def update(self):
#         self.delay += 1
#         if self.delay > 100:
#             self.delay = 0
#         if self.delay % 4 == 0:
#             self.frame = (self.frame + 1) % 17
#
#     def set_xy(self, monster):
#         self.x = monster.x
#         self.y = monster.y