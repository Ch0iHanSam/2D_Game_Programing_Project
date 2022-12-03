from pico2d import *

FD = range(1)

key_event_table = {
    (SDL_KEYDOWN, SDLK_f): FD
}

# 상호작용 클래스
class Interact:
    def __init__(self, Player, Object, bndry):
        self.image = load_image('../Effect/ETC/interact.png')
        self.x, self.y = 0, 0
        self.judge = False
        self.event_que = []
        self.Player = Player
        self.Object = Object
        self.bndry = bndry
        for i in dir(self.Object):
            if i == 'condition':
                self.condition = self.Object.condition
                break
            self.condition = True

    def draw(self):
        if self.condition:
            if self.Player.cur_name() == 'IDLE':
                if (self.Object.x + self.bndry > self.x > self.Object.x - self.bndry) and (self.Object.y + self.bndry + 10 > self.y > self.Object.y - self.bndry):
                    self.judge = True
                    self.image.draw(self.x, self.y)
                else:
                    self.judge = False

    def run(self, Object):  # Object : 상호작용 대상 / Object_Object : 대상의 대상
        Object.act()

    def update(self):
        self.x, self.y = self.Player.x, self.Player.y

        if self.event_que:  # F의 입력이 되었다면 F입력 제거하고 run함수 실행
            if self.judge:  # 상호작용 가능 거리에 있을 때만 오브젝트 작동
                self.event_que.pop()
                self.run(self.Object)
            else:
                self.event_que.pop()

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
