from pico2d import *


class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir_x = 0
        self.dir_y = 0

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):  # 원래 함수의 update 함수 역할
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:  # 원래 함수의 exdir 변수 역할
            self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
        else:
            self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == UD:
            self.dir_y += 1
        elif event == DD:
            self.dir_y -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1
        elif event == UU:
            self.dir_y -= 1
        elif event == DU:
            self.dir_y += 1

    @staticmethod
    def exit(self):
        if self.dir_x != 0:
            self.face_dir = self.dir_x

    @staticmethod
    def do(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 5 == 0:
            self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * 2.5  # 속도 리팩토리 할 때 고치기!
        self.y += self.dir_y * 2.5
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
        elif self.dir_x == 0:
            self.cur_state.exit(self)
            self.cur_state = IDLE
            self.cur_state.enter(self, None)


class PARRYING:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.image = load_image('../Object/Character/Parrying/Character_Player_Parrying.png')

    @staticmethod
    def exit(self):
        self.frame = 0
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')

    @staticmethod
    def do(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 2 == 0:
            if self.frame == 8:
                self.do = False
            self.frame = (self.frame + 1) % 9
        if self.frame == 8:
            self.cur_state.exit(self)
            self.cur_state = RUN
            self.cur_state.enter(self, None)

    @staticmethod
    def draw(self):
        if self.face_dir > 0:
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.face_dir < 0:
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)


RD, LD, UD, DD, RU, LU, UU, DU, XD = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN, SDLK_x): XD
}

next_state = {
    IDLE: {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: RUN, LD: RUN, UD: RUN, DD: RUN, XD: PARRYING},
    RUN: {RU: IDLE, LU: IDLE, UU: IDLE, DU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, DD: IDLE, XD: PARRYING},
    PARRYING: {RU: PARRYING, LU: PARRYING, UU: PARRYING, DU: PARRYING, RD: PARRYING, LD: PARRYING, UD: PARRYING,
               DD: PARRYING, XD: PARRYING}
}


class Player_Character:
    def __init__(self, x, y, face):
        self.x, self.y = x, y
        self.frame = 0
        self.dir_x, self.dir_y, self.face_dir = 0, 0, face
        self.delay = 0
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')
        self.HP = 100
        self.ATK = 10
        self.Parrying = False

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.cur_state != PARRYING:
            if self.event_que:
                event = self.event_que.pop()
                self.cur_state.exit(self)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        if self.HP <= 0:  # 죽음 확인 (아마 함수로 수정해야하지 않을까 싶음)
            self.x, self.y = 400,300
            self.HP = 100

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def check_hit(self, object_List):
        if self.cur_state == PARRYING:
            if object_List:
                for i in object_List:
                    if self.x - 30 < i.x < self.x + 30 and self.y - 50 < i.y < self.y + 10:
                        object_List.remove(i)
                        i.monster.HP -= self.ATK
        else:
            if object_List:
                for i in object_List:
                    if self.x - 30 < i.x < self.x + 30 and self.y - 50 < i.y < self.y + 10:
                        object_List.remove(i)
                        self.HP -= i.damage
