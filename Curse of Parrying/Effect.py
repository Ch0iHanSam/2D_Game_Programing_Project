from pico2d import *
import game_framework
import game_world
import math
import random

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 몬스터 공격 이펙트
class Test_Monster_Effect:
    def __init__(self, x = 0, y = 0, monster = None):
        self.x, self.y, self.frame, self.delay = x, y, 0, 0
        self.image = load_image('./Object/Enemy/Test/Effect.png')
        self.first = True
        self.Monster = monster
        self.damage = 5

    def draw(self):
        draw_rectangle(self.x - 12, self.y - 10, self.x + 12, self.y + 5)
        self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 4 == 0:
            self.frame = (self.frame + 1) % 4
        self.x += 1 * RUN_SPEED_PPS * game_framework.frame_time  # 나가는 방향이 한 방향이므로 1에 곱해줌

    def get_bb(self):
        return self.x - 12, self.y - 10, self.x + 12, self.y + 5

    def handle_collision(self, a, group):
        pass


class Monster_Attack_Effect:
    x, y, frame, t_frame, delay = None, None, 0, None, 0
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    image = None
    Monster = None
    Player = None
    dir = None
    SPEED_KMPH = 0
    SPEED_PPS = SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER


    def draw(self):
        self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.x > 900 or self.x < -100 or self.y > 700 or self.y < -100:
            game_world.remove_object(self)

        if get_time() - self.delay > 0.1:
            self.delay = get_time()
            self.frame = (self.frame + 1) % self.t_frame


        self.x += math.cos(self.dir) * self.SPEED_PPS * game_framework.frame_time
        self.y += math.sin(self.dir) * self.SPEED_PPS * game_framework.frame_time

    def get_bb(self):
        return self.x - self.min_x, self.y - self.min_y, self.x + self.max_x, self.y + self.max_y

    def handle_collision(self, b, group):
        pass


class Pigeon_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player):
        self.image = load_image('./Effect/Monster/Monster_Attack/Pigeon/Pigeon_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y
        self.min_x, self.min_y, self.max_x, self.max_y = 7,38,7,-7
        self.frame, self.t_frame, self.delay = 0, 7, get_time()
        self.SPEED_KMPH = 15
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK


class Rabbit_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player):
        self.image = load_image('./Effect/Monster/Monster_Attack/Rabbit/Rabbit_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y
        self.min_x, self.min_y, self.max_x, self.max_y = 10,10,10,10
        self.frame, self.t_frame, self.delay = 0, 1, get_time()
        self.SPEED_KMPH = 5
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK


class Crab_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player, dir_y):
        self.image = load_image('./Effect/Monster/Monster_Attack/Crab/Crab_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y-15
        self.min_x, self.min_y, self.max_x, self.max_y = 7,7,7,7
        self.frame, self.t_frame, self.delay = 0, 1, get_time()
        self.SPEED_KMPH = 7
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.ATK = Monster.ATK
        self.dir = self.Monster.dir[0]
        self.dir_y = dir_y

    def update(self):
        if get_time() - self.delay > 0.1:
            self.delay = get_time()
            self.frame = (self.frame + 1) % self.t_frame

        if self.dir != 0:
            self.x += self.dir * self.SPEED_PPS * game_framework.frame_time
            self.y += self.dir_y * self.SPEED_PPS * game_framework.frame_time
        else:
            self.x += 1 * self.SPEED_PPS * game_framework.frame_time
            self.y += self.dir_y * self.SPEED_PPS * game_framework.frame_time


class Gull_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player):
        self.image = load_image('./Effect/Monster/Monster_Attack/Gull/Gull_attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y
        self.first_x, self.first_p_x = self.Monster.x, self.Player.x
        self.min_x, self.min_y, self.max_x, self.max_y = 7,5,7,12
        self.frame, self.t_frame, self.delay = 0, 8, get_time()
        self.SPEED_KMPH = 30
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK

    def draw(self):
        if self.first_x < self.first_p_x:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        else:
            self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 68, 68)


class Turtle_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player):
        self.image = load_image('./Effect/Monster/Monster_Attack/Turtle/Turtle_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y-30
        self.min_x, self.min_y, self.max_x, self.max_y = 5, 5, 5, 5
        self.frame, self.t_frame, self.delay = 0, 1, get_time()
        self.SPEED_KMPH = float(random.randint(2, 4))
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        dir = math.atan2((random.randint(-20,20)), (random.randint(-20,20)))
        if dir == 0:
            self.dir = 1
        else:
            self.dir = dir
            del dir
        self.ATK = Monster.ATK


class Devil_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player, speed):
        self.image = load_image('./Effect/Monster/Monster_Attack/Devil/Devil_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y
        self.min_x, self.min_y, self.max_x, self.max_y = 10,10,10,10
        self.frame, self.t_frame, self.delay = 0, 1, get_time()
        self.SPEED_KMPH = 10 * speed
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK


class Vampire_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player, speed):
        self.image = load_image('./Effect/Monster/Monster_Attack/Vampire/Vampire_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y
        self.min_x, self.min_y, self.max_x, self.max_y = 7,5,7,5
        self.frame, self.t_frame, self.delay = 0, 1, get_time()
        self.SPEED_KMPH = 3 * speed
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK


class Ork_Attack(Monster_Attack_Effect):
    def __init__(self, Monster, Player, speed):
        self.image = load_image('./Effect/Monster/Monster_Attack/Ork/Ork_Attack.png')
        self.Monster = Monster
        self.Player = Player
        self.x, self.y = self.Monster.x, self.Monster.y
        self.min_x, self.min_y, self.max_x, self.max_y = 7,7,7,7
        self.frame, self.t_frame, self.delay = 0, 4, get_time()
        self.SPEED_KMPH = 5 * speed
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK


class Boss_Attack_BloodWind(Monster_Attack_Effect):
    def __init__(self, Monster, Player, dir):
        self.image = load_image('Effect/Monster/Monster_Attack/Boss/Attack_1_Effect.png')
        self.Monster = Monster
        self.Player = Player
        self.min_x, self.min_y, self.max_x, self.max_y = 5, 25, 5, 25
        self.frame, self.t_frame, self.delay = 0, 1, get_time()
        self.SPEED_KMPH = 30
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = dir
        if self.dir == 1:
            self.x, self.y = -30, self.Player.y
        elif self.dir == -1:
            self.x, self.y = 830, self.Player.y
        self.ATK = Monster.ATK

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y)
        draw_rectangle(self.x - self.min_x, self.y - self.min_y, self.x + self.max_x, self.y + self.max_y)

    def update(self):
        if get_time() - self.delay > 0.1:
            self.delay = get_time()
            self.frame = (self.frame + 1) % self.t_frame

        self.x += self.dir * self.SPEED_PPS * game_framework.frame_time


class Boss_Attack_SummonMiniBoss(Monster_Attack_Effect):
    def __init__(self, Monster, Player, location):
        self.image = load_image('Effect/Monster/Monster_Attack/Boss/Attack_2_Effect.png')
        self.Monster = Monster
        self.Player = Player
        if location == 'right':
            self.x, self.y = self.Monster.x + 50, self.Monster.y
        elif location == 'left':
            self.x, self.y = self.Monster.x - 50, self.Monster.y
        elif location == 'up':
            self.x, self.y = self.Monster.x, self.Monster.y + 50
        elif location == 'down':
            self.x, self.y = self.Monster.x, self.Monster.y - 50
        self.min_x, self.min_y, self.max_x, self.max_y = 10, 10, 10, 10
        self.frame, self.t_frame, self.delay = 0, 7, get_time()
        self.SPEED_KMPH = 3 + random.randint(1, 4)
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        self.ATK = Monster.ATK

    def update(self):
        self.dir = math.atan2((self.Player.y - self.Monster.y), (self.Player.x - self.Monster.x))
        if get_time() - self.delay > 0.1:
            self.delay = get_time()
            self.frame = (self.frame + 1) % self.t_frame


        self.x += math.cos(self.dir) * self.SPEED_PPS * game_framework.frame_time
        self.y += math.sin(self.dir) * self.SPEED_PPS * game_framework.frame_time


# 인터페이스
#HP
class HP:
    def __init__(self, Player):
        self.Player = Player
        if Player.HP == 100:
            self.image = load_image('./Effect/Character/HP/HP=100.png')
        elif Player.HP == 95:
            self.image = load_image('./Effect/Character/HP/HP=95.png')
        elif Player.HP == 90:
            self.image = load_image('./Effect/Character/HP/HP=90.png')
        elif Player.HP == 85:
            self.image = load_image('./Effect/Character/HP/HP=85.png')
        elif Player.HP == 80:
            self.image = load_image('./Effect/Character/HP/HP=80.png')
        elif Player.HP == 75:
            self.image = load_image('./Effect/Character/HP/HP=75.png')
        elif Player.HP == 70:
            self.image = load_image('./Effect/Character/HP/HP=70.png')
        elif Player.HP == 65:
            self.image = load_image('./Effect/Character/HP/HP=65.png')
        elif Player.HP == 60:
            self.image = load_image('./Effect/Character/HP/HP=60.png')
        elif Player.HP == 55:
            self.image = load_image('./Effect/Character/HP/HP=55.png')
        elif Player.HP == 50:
            self.image = load_image('./Effect/Character/HP/HP=50.png')
        elif Player.HP == 45:
            self.image = load_image('./Effect/Character/HP/HP=45.png')
        elif Player.HP == 40:
            self.image = load_image('./Effect/Character/HP/HP=40.png')
        elif Player.HP == 35:
            self.image = load_image('./Effect/Character/HP/HP=35.png')
        elif Player.HP == 30:
            self.image = load_image('./Effect/Character/HP/HP=30.png')
        elif Player.HP == 25:
            self.image = load_image('./Effect/Character/HP/HP=25.png')
        elif Player.HP == 20:
            self.image = load_image('./Effect/Character/HP/HP=20.png')
        elif Player.HP == 15:
            self.image = load_image('./Effect/Character/HP/HP=15.png')
        elif Player.HP == 10:
            self.image = load_image('./Effect/Character/HP/HP=10.png')
        elif Player.HP == 5:
            self.image = load_image('./Effect/Character/HP/HP=5.png')
        self.x = 110
        self.y = 490

    def update(self):
        if self.Player.HP == 100:
            self.image = load_image('./Effect/Character/HP/HP=100.png')
        elif self.Player.HP == 95:
            self.image = load_image('./Effect/Character/HP/HP=95.png')
        elif self.Player.HP == 90:
            self.image = load_image('./Effect/Character/HP/HP=90.png')
        elif self.Player.HP == 85:
            self.image = load_image('./Effect/Character/HP/HP=85.png')
        elif self.Player.HP == 80:
            self.image = load_image('./Effect/Character/HP/HP=80.png')
        elif self.Player.HP == 75:
            self.image = load_image('./Effect/Character/HP/HP=75.png')
        elif self.Player.HP == 70:
            self.image = load_image('./Effect/Character/HP/HP=70.png')
        elif self.Player.HP == 65:
            self.image = load_image('./Effect/Character/HP/HP=65.png')
        elif self.Player.HP == 60:
            self.image = load_image('./Effect/Character/HP/HP=60.png')
        elif self.Player.HP == 55:
            self.image = load_image('./Effect/Character/HP/HP=55.png')
        elif self.Player.HP == 50:
            self.image = load_image('./Effect/Character/HP/HP=50.png')
        elif self.Player.HP == 45:
            self.image = load_image('./Effect/Character/HP/HP=45.png')
        elif self.Player.HP == 40:
            self.image = load_image('./Effect/Character/HP/HP=40.png')
        elif self.Player.HP == 35:
            self.image = load_image('./Effect/Character/HP/HP=35.png')
        elif self.Player.HP == 30:
            self.image = load_image('./Effect/Character/HP/HP=30.png')
        elif self.Player.HP == 25:
            self.image = load_image('./Effect/Character/HP/HP=25.png')
        elif self.Player.HP == 20:
            self.image = load_image('./Effect/Character/HP/HP=20.png')
        elif self.Player.HP == 15:
            self.image = load_image('./Effect/Character/HP/HP=15.png')
        elif self.Player.HP == 10:
            self.image = load_image('./Effect/Character/HP/HP=10.png')
        elif self.Player.HP == 5:
            self.image = load_image('./Effect/Character/HP/HP=5.png')

    def draw(self):
        self.image.draw(self.x, self.y, 200, 200)

#일시정지
class Pause:
    def __init__(self):
        self.x, self.y = 770, 570
        self.image = load_image('./BackGround/Pause_Mark.png')

    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)

    def update(self):
        pass