from pico2d import *
import game_world
import game_framework
import stage_home_state

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# class IDLE:
#     @staticmethod
#     def enter(self, event):
#         self.dir_x = 0
#         self.dir_y = 0
#
#     @staticmethod
#     def exit(self):
#         pass
#
#     @staticmethod
#     def do(self):  # 원래 함수의 update 함수 역할
#         pass
#
#     @staticmethod
#     def draw(self):
#         if self.face_dir == 1:  # 원래 함수의 exdir 변수 역할
#             self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
#         else:
#             self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        if event == RD:
            self.dir_x += 1
        if event == LD:
            self.dir_x -= 1
        if event == UD:
            self.dir_y += 1
        if event == DD:
            self.dir_y -= 1
        if event == RU:
            self.dir_x -= 1
        if event == LU:
            self.dir_x += 1
        if event == UU:
            self.dir_y -= 1
        if event == DU:
            self.dir_y += 1

    @staticmethod
    def exit(self):
        if self.dir_x != 0:
            self.face_dir = self.dir_x

    @staticmethod
    def do(self):
        if get_time() - self.delay > 0.1:
            self.delay = get_time()
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time


        self.x = clamp(50, self.x, 750)
        self.y = clamp(78, self.y, 578)

    @staticmethod
    def draw(self):
        if self.dir_x > 0:  # 오른쪽
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir_x < 0:  # 왼쪽
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_y > 0:  # 위
            if self.face_dir > 0:  # 오른쪽 바라봄
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.face_dir < 0:  # 왼쪽 바라봄
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir_y < 0:  # 아래
            if self.face_dir > 0:  # 오른쪽 바라봄
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.face_dir < 0:  # 왼쪽 바라봄
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        if self.dir_x == 0 and self.dir_y == 0:
            if self.face_dir == 1:  # 원래 함수의 exdir 변수 역할
                self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
            else:
                self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)


class PARRYING:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.image = load_image('./Object/Character/Parrying/Character_Player_Parrying.png')

    @staticmethod
    def exit(self):
        self.frame = 0
        self.image = load_image('./Object/Character/Walking/Character_Player_Walking.png')

    @staticmethod
    def do(self):
        if get_time() - self.delay > 0.05:
            self.delay = get_time()
            self.frame = (self.frame + 1) % 9
        if self.frame == 8:
            self.cur_state.exit(self)
            self.cur_state = RUN
            self.cur_state.enter(self, None)
            self.cur_state.draw(self)  # 들어가서 맨 처음 안그리니까 깜박거리는거 해결하기 위해 작성

    @staticmethod
    def draw(self):
        if self.face_dir > 0:
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.face_dir < 0:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)


class DASH:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.image = load_image('./Object/Character/Parrying/Character_Player_Parrying.png')

    @staticmethod
    def exit(self):
        self.frame = 0
        self.image = load_image('./Object/Character/Walking/Character_Player_Walking.png')

    @staticmethod
    def do(self):
        if get_time() - self.delay > 0.007:
            self.delay = get_time()
            self.frame = (self.frame + 1) % 9
        if self.frame == 8:
            self.cur_state.exit(self)
            self.cur_state = RUN
            self.cur_state.enter(self, None)
            self.cur_state.draw(self)  # 들어가서 맨 처음 안그리니까 깜박거리는거 해결하기 위해 작성
        if self.dir_x == 0 and self.dir_y == 0:
            self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time * 2.5
        else:
            self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time * 2.5
            self.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time * 2.5

        self.x = clamp(50, self.x, 750)
        self.y = clamp(78, self.y, 578)

    @staticmethod
    def draw(self):
        if self.face_dir > 0:
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.face_dir < 0:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)


RD, LD, UD, DD, RU, LU, UU, DU, XD, ZD = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN, SDLK_x): XD,
    (SDL_KEYDOWN, SDLK_z): ZD
}

next_state = {
    # IDLE: {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: RUN, LD: RUN, UD: RUN, DD: RUN, XD: PARRYING},
    RUN: {RU: RUN, LU: RUN, UU: RUN, DU: RUN, RD: RUN, LD: RUN, UD: RUN, DD: RUN, XD: PARRYING, ZD: DASH},
    PARRYING: {RU: PARRYING, LU: PARRYING, UU: PARRYING, DU: PARRYING, RD: PARRYING, LD: PARRYING, UD: PARRYING,
               DD: PARRYING, XD: PARRYING, ZD: PARRYING},
    DASH: {RU: DASH, LU: DASH, UU: DASH, DU: DASH, RD: DASH, LD: DASH, UD: DASH, DD: DASH, XD: DASH, ZD: DASH}
}


class Player_Character:
    def __init__(self, x, y, face):
        self.x, self.y = x, y
        self.frame = 0
        self.dir_x, self.dir_y, self.face_dir = 0, 0, face
        self.delay = get_time()
        self.image = load_image('./Object/Character/Walking/Character_Player_Walking.png')
        self.HP = 100
        self.ATK = 10
        self.Parrying = False

        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)
        self.exist = True

    def update(self):
        self.cur_state.do(self)

        if self.cur_state == RUN:
            if self.event_que:
                event = self.event_que.pop()
                self.cur_state.exit(self)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(self.x-15, self.y-35, self.x+15, self.y - 10)
        if self.HP <= 0:  # 죽음 확인 (아마 함수로 수정해야하지 않을까 싶음)
            self.x, self.y = 400, 300
            self.HP = 100

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def cur_name(self):
        if self.dir_x == 0 and self.dir_y == 0:
            return 'IDLE'
        elif self.cur_state == RUN:
            return 'RUN'
        elif self.cur_state == PARRYING:
            return 'PARRYING'
        elif self.cur_state == DASH:
            return 'DASH'

    def set_xy(self, x, y, face):
        self.x = x
        self.y = y
        self.face_dir = face

    def get_bb(self):
        return self.x - 15, self.y - 35, self.x + 15, self.y -10

    def handle_collision(self, b, group):
        if group == 'player:attack':
            if self.cur_state == PARRYING or self.cur_state == DASH:
                if b in game_world.objects[4]:  # 이펙트면 이펙트 지우기
                    game_world.remove_object(b)
                    b.Monster.HP -= self.ATK

                elif b in game_world.objects[3]:  # 몸통박치기면 attack만 False로 바꾸기
                    if b.attack:
                        b.HP -= self.ATK
                        b.attack = False

            else:
                if b in game_world.objects[4]:
                    game_world.remove_object(b)
                    self.HP -= b.ATK

                elif b in game_world.objects[3]:  # 몸통박치기면 attack만 False로 바꾸기
                    if b.attack:
                        self.HP -= b.ATK
                        b.attack = False

        elif group == 'player:npc':
            pass