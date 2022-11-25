from pico2d import *
import game_framework
import conversation_state

class Portal:

    def __init__(self, name, x, y):
        self.image = load_image(name)
        self.frame = 0
        self.delay = 0
        self.x, self.y = x, y
        self.this_stage = ''
        self.out_stage = ''

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 5 == 0:
            self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 100, 100)
        # draw_rectangle(self.x-25, self.y-30, self.x+25, self.y+2)

    def check_enter(self, Player, state, min_x, max_x, min_y, max_y, this_stage_name, out_stage_name):
        if self.x + min_x  < Player.x < self.x + max_x and self.y + min_y < Player.y < self.y + max_y:
            self.this_stage = this_stage_name
            self.out_stage = out_stage_name
            game_framework.change_state(state)


    def this_stage_name(self):
        return self.this_stage

    def out_stage_name(self):
        return self.out_stage


class Test_Monster_Box:
    def __init__(self, x, y, Monster):
        self.x, self.y = x, y
        self.image = load_image('../Object/ETC/MonsterBox.png')
        self.monster = Monster

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def act(self):
        self.monster.set_summon()

#NPC
class Unknown:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.image = load_image('../Object/NPC/NPC_UNKNOWN.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def act(self):
        game_framework.push_state(conversation_state)