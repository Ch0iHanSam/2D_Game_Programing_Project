from pico2d import *
import game_framework
import game_world
import random

PIXEL_PER_METER = (10.0 / 0.3)
time = 0

class Test_Monster:
    def __init__(self, x=200, y=100):
        self.x, self.y, self.frame = x, y, 0
        self.image = load_image('./Object/Enemy/Test/Enemy_Test_Attack.png')
        self.summon = False
        self.delay = 0
        self.attack = False
        self.val_check_attack = 0  # 어택 변환 용으로 사용됨. 다른 곳에 사용되지 않음
        self.HP = 30
        self.ATK = 5

    def draw(self):
        if self.summon:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.HP <= 0:
            self.summon = False
            self.HP = 30
        if self.summon:
            self.delay += 1
            if self.delay == 100:
                self.delay = 0
            if self.delay % 6 == 0:
                self.frame = (self.frame + 1) % 10
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


class Monster:
    image = None
    image_normal, image_attack = None, None
    x, y, frame, delay, t_frame = None, None, 0, get_time(), None  # t_frame : total frame
    frame_normal, frame_attack = None, None
    HP = None  # 체력
    ATK = None  # 공격력
    SPEED_KMPH = 0
    SPEED_PPS = SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
    first = True
    attack = False
    behavior = False  # False : move, True : attack
    move_end = None
    dir = None
    move_time = None

    def draw(self):
        if self.first:
            magic_circle = load_image('./Effect/Monster/Effect_Summon.png')
            magic_circle.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            if self.frame == 15:
                self.first = False
        else:
            if self.dir[0] > -1:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            else:
                self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 68, 68)

    def update(self):
        if self.first:
            if get_time() - self.delay > 0.005:
                self.delay = get_time()
                self.frame = (self.frame + 1) % 16
        else:
            if get_time() - self.delay > 0.1:
                self.delay = get_time()
                self.frame = (self.frame + 1) % self.t_frame

        if not self.first:
            if self.behavior:
                self.set_attack()
            else:
                self.set_move()

        self.death()

    def set_move(self):
        self.image = load_image(self.image_normal)
        self.t_frame = self.frame_normal

        self.x += self.dir[0] * self.SPEED_PPS * game_framework.frame_time
        self.y += self.dir[1] * self.SPEED_PPS * game_framework.frame_time

        self.x = clamp(70, self.x, 720)
        self.y = clamp(100, self.y, 550)

        if get_time() - self.move_time > self.move_end:
            self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
            if self.x == 70:
                self.dir[0] = 1
            elif self.x == 720:
                self.dir[0] = -1
            if self.y == 100:
                self.dir[1] = 1
            elif self.y == 550:
                self.dir[1] = -1

            self.move_end = random.randint(2, 5)
            self.behavior = True
            self.frame = 0

    def set_attack(self):
        if self.frame == 2:
            if not self.attack:  # 최초 1회만 어택 발동하게
                self.image = load_image(self.image_attack)
                self.t_frame = self.frame_attack
                self.attack = True
                self.frame = 3
        else:
            self.attack = False

        if self.frame == self.frame_attack - 1:
            self.behavior = False
            self.attack = False
            self.frame = 0
            self.move_time = get_time()

    def death(self):
        if self.HP <= 0:
            game_world.remove_object(self)


class Pigeon(Monster):
    def __init__(self):
        self.image = load_image('./Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Fly.png')
        self.image_normal = './Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Fly.png'
        self.image_attack = './Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 7
        self.frame_normal = 7
        self.frame_attack = 9
        self.HP = 20
        self.ATK = 5
        self.SPEED_KMPH = 10.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0


class Boar(Monster):
    def __init__(self, Player):
        self.image = load_image('./Object/Enemy/Stage1/Boar/Enemy_Boar_Move.png')
        self.image_normal = './Object/Enemy/Stage1/Boar/Enemy_Boar_Move.png'
        self.image_attack = './Object/Enemy/Stage1/Boar/Enemy_Boar_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 6
        self.frame_normal = 6
        self.frame_attack = 16
        self.HP = 40
        self.ATK = 20
        self.SPEED_KMPH = 5.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0
        self.attack_random = True
        self.Player = Player
        self.set_dir = True

    def set_attack(self):
        self.image = load_image(self.image_attack)
        self.t_frame = self.frame_attack
        dir = math.atan2((self.Player.y - self.y), (self.Player.x - self.x))

        if self.frame == 1:
            self.attack = True
            self.frame = 2

        for i in game_world.objects[3]:
            if type(i) != Boar:
                self.attack_random = True
                break
            self.attack_random = False

        if self.attack_random:
            self.x += self.dir[0] * self.SPEED_PPS * game_framework.frame_time * 3
            self.y += self.dir[1] * self.SPEED_PPS * game_framework.frame_time * 3
        else:
            if self.set_dir:
                if self.x > self.Player.x: self.dir[0] = -1
                else: self.dir[0] = 1
                self.set_dir = False
            self.x += math.cos(dir) * self.SPEED_PPS * game_framework.frame_time * 3
            self.y += math.sin(dir) * self.SPEED_PPS * game_framework.frame_time * 3

        self.x = clamp(70, self.x, 720)
        self.y = clamp(100, self.y, 550)

        if self.x == 70:
            self.dir[0] = 1
        elif self.x == 720:
            self.dir[0] = -1
        if self.y == 100:
            self.dir[1] = 1
        elif self.y == 550:
            self.dir[1] = -1

        if self.frame == self.frame_attack - 1:
            self.attack = False
            self.behavior = False
            self.frame = 0
            self.move_time = get_time()
            self.set_dir = True

    def get_bb(self):
        return self.x - 23, self.y - 35, self.x + 23, self.y - 8

    def handle_collision(self, b, group):
        pass


class Rabbit(Monster):
    def __init__(self):
        self.image = load_image('./Object/Enemy/Stage1/Rabbit/Enemy_Rabbit_Move.png')
        self.image_normal = './Object/Enemy/Stage1/Rabbit/Enemy_Rabbit_Move.png'
        self.image_attack = './Object/Enemy/Stage1/Rabbit/Enemy_Rabbit_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 7
        self.frame_normal = 7
        self.frame_attack = 10
        self.HP = 10
        self.ATK = 10
        self.SPEED_KMPH = 7.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0


class Crab(Monster):
    def __init__(self):
        self.image = load_image('./Object/Enemy/Stage2/Crab/Enemy_Crab_Move.png')
        self.image_normal = './Object/Enemy/Stage2/Crab/Enemy_Crab_Move.png'
        self.image_attack = './Object/Enemy/Stage2/Crab/Enemy_Crab_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 4
        self.frame_normal = 4
        self.frame_attack = 10
        self.HP = 20
        self.ATK = 10
        self.SPEED_KMPH = 5.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), 0]
        self.move_end = random.randint(2, 5)
        self.move_time = 0

    def set_move(self):
        self.image = load_image(self.image_normal)
        self.t_frame = self.frame_normal

        self.x += self.dir[0] * self.SPEED_PPS * game_framework.frame_time

        self.x = clamp(70, self.x, 720)
        self.y = clamp(100, self.y, 550)

        if get_time() - self.move_time > self.move_end:
            self.dir = [random.randint(-1, 1), 0]
            if self.x == 70:
                self.dir[0] = 1
            elif self.x == 720:
                self.dir[0] = -1
            if self.y == 100:
                self.dir[1] = 1
            elif self.y == 550:
                self.dir[1] = -1

            self.move_end = random.randint(2, 5)
            self.behavior = True
            self.frame = 0


class Gull(Monster):
    def __init__(self):
        self.image = load_image('./Object/Enemy/Stage2/Gull/Enemy_Gull_Fly.png')
        self.image_normal = './Object/Enemy/Stage2/Gull/Enemy_Gull_Fly.png'
        self.image_attack = './Object/Enemy/Stage2/Gull/Enemy_Gull_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 4
        self.frame_normal = 4
        self.frame_attack = 6
        self.HP = 20
        self.ATK = 5
        self.SPEED_KMPH = 15.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0


class Turtle(Monster):
    def __init__(self):
        self.image = load_image('./Object/Enemy/Stage2/Turtle/Enemy_Turtle_Move.png')
        self.image_normal = './Object/Enemy/Stage2/Turtle/Enemy_Turtle_Move.png'
        self.image_attack = './Object/Enemy/Stage2/Turtle/Enemy_Turtle_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 4
        self.frame_normal = 4
        self.frame_attack = 8
        self.HP = 100
        self.ATK = 10
        self.SPEED_KMPH = 2.5
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0
        self.attack_random = True
        self.set_dir = True

    def draw(self):
        if self.first:
            magic_circle = load_image('./Effect/Monster/Effect_Summon.png')
            magic_circle.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            if self.frame == 15:
                self.first = False
        else:
            if self.dir[0] > -1:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 120, 120)
            else:
                self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 120, 120)


class Vampire(Monster):
    def __init__(self):
        self.image = load_image('./Object/Enemy/Stage3/Vampire/Enemy_Vampire_Move.png')
        self.image_normal = './Object/Enemy/Stage3/Vampire/Enemy_Vampire_Move.png'
        self.image_attack = './Object/Enemy/Stage3/Vampire/Enemy_Vampire_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 4
        self.frame_normal = 4
        self.frame_attack = 28
        self.HP = 70
        self.ATK = 30
        self.SPEED_KMPH = 10.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0

    def draw(self):
        if self.first:
            magic_circle = load_image('./Effect/Monster/Effect_Summon.png')
            magic_circle.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            if self.frame == 15:
                self.first = False
        else:
            if self.dir[0] > -1:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 150, 150)
            else:
                self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 150, 150)


class Devil(Monster):
    def __init__(self):
        self.image = load_image('Object/Enemy/Stage3/Devil/Enemy_Devil_Move.png')
        self.image_normal = 'Object/Enemy/Stage3/Devil/Enemy_Devil_Move.png'
        self.image_attack = 'Object/Enemy/Stage3/Devil/Enemy_Devil_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 4
        self.frame_normal = 4
        self.frame_attack = 5
        self.HP = 50
        self.ATK = 5
        self.SPEED_KMPH = 10.0
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0

    def draw(self):
        if self.first:
            magic_circle = load_image('./Effect/Monster/Effect_Summon.png')
            magic_circle.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            if self.frame == 15:
                self.first = False
        else:
            if self.dir[0] > -1:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 120, 120)
            else:
                self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 120, 120)


class Ork(Monster):
    def __init__(self):
        self.image = load_image('Object/Enemy/Stage3/Ork/Enemy_Ork_Move.png')
        self.image_normal = 'Object/Enemy/Stage3/Ork/Enemy_Ork_Move.png'
        self.image_attack = 'Object/Enemy/Stage3/Ork/Enemy_Ork_Attack.png'
        self.x, self.y, self.t_frame = 100 + random.randint(0, 11) * 40, 200 + random.randint(0, 11) * 20, 9
        self.frame_normal = 9
        self.frame_attack = 9
        self.HP = 100
        self.ATK = 20
        self.SPEED_KMPH = 2.5
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = random.randint(2, 5)
        self.move_time = 0

    def draw(self):
        if self.first:
            magic_circle = load_image('./Effect/Monster/Effect_Summon.png')
            magic_circle.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            if self.frame == 15:
                self.first = False
        else:
            if self.dir[0] > -1:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 110, 110)
            else:
                self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 110, 110)


class Boss(Monster):
    def __init__(self):
        self.image = load_image('Object/Boss/Boss_1_Move.png')
        self.image_normal = 'Object/Boss/Boss_1_Move.png'
        self.image_attack_1 = 'Object/Boss/Boss_1_Attack1.png'
        self.image_attack_2 = 'Object/Boss/Boss_1_Attack2.png'
        self.image_attack_3 = 'Object/Boss/Boss_1_Attack3.png'
        self.x, self.y, self.t_frame = 400, 500, 8
        self.frame_normal = 8
        self.frame_attack_1 = 9
        self.frame_attack_2 = 16
        self.frame_attack_3 = 15
        self.HP = 200
        self.ATK = 20
        self.SPEED_KMPH = 10
        self.SPEED_PPS = self.SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER
        self.first = True
        self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
        self.move_end = 1
        self.move_time = 0
        self.behavior = 'MOVE'

    def draw(self):
        if self.first:
            magic_circle = load_image('./Effect/Monster/Effect_Summon.png')
            magic_circle.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 200, 200)
            if self.frame == 15:
                self.first = False
        else:
            if self.dir[0] > -1:
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
            else:
                self.image.clip_composite_draw(self.frame * 68, 0, 68, 68, 0, 'h', self.x, self.y, 68, 68)

    def update(self):
        if self.first:
            if get_time() - self.delay > 0.005:
                self.delay = get_time()
                self.frame = (self.frame + 1) % 16
        else:
            if get_time() - self.delay > 0.1:
                self.delay = get_time()
                self.frame = (self.frame + 1) % self.t_frame

        if not self.first:
            if self.behavior == 'MOVE':
                self.set_move()
            elif self.behavior == 'ATTACK_1':
                self.set_attack_1()
            elif self.behavior == 'ATTACK_2':
                self.set_attack_2()
            elif self.behavior == 'ATTACK_3':
                self.set_attack_3()

        self.death()

    def set_move(self):
        self.image = load_image(self.image_normal)
        self.t_frame = self.frame_normal

        self.x += self.dir[0] * self.SPEED_PPS * game_framework.frame_time
        self.y += self.dir[1] * self.SPEED_PPS * game_framework.frame_time

        self.x = clamp(70, self.x, 720)
        self.y = clamp(100, self.y, 550)

        if get_time() - self.move_time > self.move_end:
            self.dir = [random.randint(-1, 1), random.randint(-1, 1)]
            if self.x == 70:
                self.dir[0] = 1
            elif self.x == 720:
                self.dir[0] = -1
            if self.y == 100:
                self.dir[1] = 1
            elif self.y == 550:
                self.dir[1] = -1


            bh = random.randint(1,3)
            if bh == 1:
                self.behavior = 'ATTACK_1'
            elif bh == 2:
                self.behavior = 'ATTACK_2'
            elif bh == 3:
                self.behavior = 'ATTACK_3'
            self.frame = 0

    def set_attack_1(self):
        if self.frame == 1:
            if not self.attack:  # 최초 1회만 어택 발동하게
                self.image = load_image(self.image_attack_1)
                self.t_frame = self.frame_attack_1
                self.attack = True
                self.frame = 2
        else:
            self.attack = False

        if self.frame == self.frame_attack_1 - 1:
            self.behavior = 'MOVE'
            self.attack = False
            self.frame = 0
            self.move_time = get_time()

    def set_attack_2(self):
        if self.frame == 1:
            if not self.attack:  # 최초 1회만 어택 발동하게
                self.image = load_image(self.image_attack_2)
                self.t_frame = self.frame_attack_2
                self.attack = True
                self.frame = 2
        else:
            self.attack = False

        if self.frame == self.frame_attack_2 - 1:
            self.behavior = 'MOVE'
            self.attack = False
            self.frame = 0
            self.move_time = get_time()

    def set_attack_3(self):
        if self.frame == 1:
            if not self.attack:  # 최초 1회만 어택 발동하게
                self.image = load_image(self.image_attack_3)
                self.t_frame = self.frame_attack_3
                self.attack = True
                self.frame = 3
        else:
            self.attack = False

        if self.frame == self.frame_attack_3 - 1:
            self.behavior = 'MOVE'
            self.attack = False
            self.frame = 0
            self.move_time = get_time()

    def death(self):
        if self.HP <= 0:
            game_world.remove_object(self)