from pico2d import *
import game_framework
import stage_castle_state
import stage_forest_state
import pause_state
from Player import Player_Character
from Background import Beach_Stage
import Object
import Enemy
from Interact import Interact
import Shield
import Effect
import server
import game_world
import random



class Fu_Va:
    check_clear = server.check_clear

    @staticmethod
    def handle_event_Button(event):
        for i in game_world.objects[5]:
            i.handle_event(event)

    @staticmethod
    def Portal_update():
        if Fu_Va.check_clear:
            server.Portal_Up.check_enter(server.Player, stage_castle_state, -25, 25, 45, 85)

    @staticmethod
    def select_Monster():
        server.Monsters = []

        for i in range(10):
            monster = random.randint(1,5)
            if monster == 1 or monster == 2:
                server.Monsters.append(Enemy.Crab())
            elif monster == 3:
                server.Monsters.append(Enemy.Turtle())
            elif monster == 4 or monster == 5:
                server.Monsters.append(Enemy.Gull())

        game_world.add_objects(server.Monsters, 3)

    @staticmethod
    def add_Attack_Effect():
        for monster in game_world.objects[3]:
            if monster.attack:
                if type(monster) == Enemy.Crab:
                    effect_up = Effect.Crab_Attack(monster, Player, 0.5)
                    effect_down = Effect.Crab_Attack(monster, Player, -0.5)
                    game_world.add_object(effect_up, 4)
                    game_world.add_object(effect_down, 4)
                    game_world.add_collision_pairs(None, effect_up, 'player:attack')
                    game_world.add_collision_pairs(None, effect_down, 'player:attack')
                elif type(monster) == Enemy.Turtle:
                    effects = [Effect.Turtle_Attack(monster, Player) for i in range(5)]
                    game_world.add_objects(effects, 4)
                    for i in effects:
                        game_world.add_collision_pairs(None, i, 'player:attack')
                elif type(monster) == Enemy.Gull:
                    effect = Effect.Gull_Attack(monster, Player)
                    game_world.add_object(effect, 4)
                    game_world.add_collision_pairs(None, effect, 'player:attack')

    @staticmethod
    def collide(a, b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        return True

    @staticmethod
    def clear():
        if not Fu_Va.check_clear:
            if len(game_world.objects[3]) == 0:
                server.HP_Crystal = Object.HP_Crystal(400, 300, Player)  # Player ????????? ?????? Player ?????? ????????? ??????
                game_world.add_object(server.HP_Crystal, 1)
                server.Button_HP_Crystal = Interact(Player, server.HP_Crystal, 30)
                game_world.add_object(server.Button_HP_Crystal, 5)
                server.Portal_Up = Object.Portal('./Object/ETC/Portal_UP.png', 400, 507)
                game_world.add_object(server.Portal_Up, 1)

                Fu_Va.check_clear = True




Player = None  # ????????????


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):  # ????????????
            if 750 < event.x < 790 and 10 < event.y < 50:
                game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):  # ????????????
            Fu_Va.handle_event_Button(event)
        else:
            Player.handle_event(event)  # ?????????????????? ???????????? ?????????


def enter():
    global Player
    Player = server.Player
    Player.set_xy(400, 120, 1)
    game_world.add_object(Player, 1)
    server.Background = Beach_Stage()
    game_world.add_object(server.Background, 0)
    Fu_Va.select_Monster()  # ????????? ?????? (?????? ????????? add_object ?????? ??? ?????????)
    Fu_Va.check_clear = server.check_clear


    # ???????????????
    server.HP = Effect.HP(Player)
    game_world.add_object(server.HP, 6)
    server.Pause = Effect.Pause()
    game_world.add_object(server.Pause, 6)

    # ??????
    game_world.add_collision_pairs(Player, None, 'player:attack')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if Fu_Va.collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    Fu_Va.clear()
    Fu_Va.add_Attack_Effect()
    Fu_Va.Portal_update()  # ?????? ??????????????? ?????? ????????????(exit????????? ?????? ???????????? ???????????? ????????? ??? ?????? ?????? ?????? update??? ????????? ?????????)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.01)

def pause():
    pass

def resume():
    pass


# ?????? ??????
def test_self():
    import stage_forest_state

    pico2d.open_canvas()
    game_framework.run(stage_forest_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()