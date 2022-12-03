from pico2d import *
import game_framework
import conversation_state
import game_world


class Portal:

    def __init__(self, name, x, y):
        self.image = load_image(name)
        self.frame = 0
        self.delay = 0
        self.x, self.y = x, y

    def update(self):
        self.delay += 1
        if self.delay > 100:
            self.delay = 0
        if self.delay % 5 == 0:
            self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y, 100, 100)
        # draw_rectangle(self.x-25, self.y-30, self.x+25, self.y+2)

    def check_enter(self, Player, state, min_x, max_x, min_y, max_y):
        if self.x + min_x < Player.x < self.x + max_x and self.y + min_y < Player.y < self.y + max_y:
            game_framework.change_state(state)


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
        self.monster.HP = 30


# NPC
class Unknown:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.image = load_image('../Object/NPC/NPC_UNKNOWN.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def act(self):
        game_framework.push_state(conversation_state)


class HP_Crystal:
    def __init__(self, x=0, y=0, Player=None):
        self.x, self.y, self.frame = x, y, 0
        self.image = load_image('../Object/NPC/NPC_HPCRYSTAL.png')
        self.delay = get_time()
        self.player = Player
        self.condition = False

    def draw(self):
        if len(game_world.objects[3]) == 0:
            self.condition = True
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        else:
            self.condition = False

    def update(self):
        if get_time() - self.delay > 0.1:
            self.delay = get_time()
            self.frame = (self.frame + 1) % 10

    def act(self):  # 풀체력 회복
        self.player.HP = 100
