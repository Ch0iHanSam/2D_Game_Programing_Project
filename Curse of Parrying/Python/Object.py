from pico2d import *
import game_framework


class Portal:

    def __init__(self, name, x, y):
        self.image = load_image(name)
        self.frame = 0
        self.delay = 0
        self.x, self.y = x, y
        self.next_stage = ''

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 5 == 0:
            self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 100, 100)

    def check_enter(self, Player, state, min_x, max_x, min_y, max_y, stage_name):
        if self.x + min_x  < Player.x < self.x + max_x and self.y - min_y < Player.y < self.y + max_y:
            self.next_stage = stage_name
            game_framework.change_state(state)


    def next_stage_name(self):
        return self.next_stage


# # 몬스터박스 클래스
# class MonsterBox:
#     def __init__(self):
#         self.image = load_image('../Object/ETC/MonsterBox.png')
#         self.x, self.y = 600, 500
#
#     def draw(self):
#         self.image.draw(self.x, self.y)
#
#
# # 몬스터박스2 클래스
# class MonsterBox2:
#     def __init__(self):
#         self.image = load_image('../Object/ETC/MonsterBox2.png')
#         self.x, self.y = 500, 500
#
#     def draw(self):
#         self.image.draw(self.x, self.y)