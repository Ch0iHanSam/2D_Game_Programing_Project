from pico2d import *
import game_framework
import clear_state
import stage_beach_state
import pause_state
from Player import Player_Character
from Background import Castle_Stage
import Object
import Enemy
from Interact import Interact
import Shield
import Effect
import server
import game_world
import random



class Fu_Va:
    phase_1 = server.phase_1
    phase_2 = server.phase_2

    @staticmethod
    def handle_event_Button(event):
        for i in game_world.objects[5]:
            i.handle_event(event)

    @staticmethod
    def Portal_update():
        if not Fu_Va.phase_2 and Fu_Va.phase_1:
            server.Portal_Up.check_enter(server.Player, clear_state, -25, 25, 45, 85)

    @staticmethod
    def select_Monster():
        server.Monsters = []

        for i in range(10):
            monster = random.randint(1,5)
            if monster == 1 or monster == 2:
                server.Monsters.append(Enemy.Devil())
            elif monster == 3:
                server.Monsters.append(Enemy.Ork())
            elif monster == 4 or monster == 5:
                server.Monsters.append(Enemy.Vampire())

        game_world.add_objects(server.Monsters, 3)

    @staticmethod
    def add_Attack_Effect():
        for monster in game_world.objects[3]:
            if monster.attack:
                if type(monster) == Enemy.Vampire:
                    effect = Effect.Vampire_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    effect2 = Effect.Vampire_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    effect3 = Effect.Vampire_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    game_world.add_object(effect, 4)
                    game_world.add_object(effect2, 4)
                    game_world.add_object(effect3, 4)
                    game_world.add_collision_pairs(None, effect, 'player:attack')
                    game_world.add_collision_pairs(None, effect2, 'player:attack')
                    game_world.add_collision_pairs(None, effect3, 'player:attack')
                elif type(monster) == Enemy.Ork:
                    effect = Effect.Ork_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    effect2 = Effect.Ork_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    game_world.add_object(effect, 4)
                    game_world.add_object(effect2, 4)
                    game_world.add_collision_pairs(None, effect, 'player:attack')
                    game_world.add_collision_pairs(None, effect2, 'player:attack')
                elif type(monster) == Enemy.Devil:
                    effect = Effect.Devil_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    effect2 = Effect.Devil_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    effect3 = Effect.Devil_Attack(monster, Player, random.choice([0.3, 0.5, 0.8, 1.0, 1.2]))
                    game_world.add_object(effect, 4)
                    game_world.add_object(effect2, 4)
                    game_world.add_object(effect3, 4)
                    game_world.add_collision_pairs(None, effect, 'player:attack')
                    game_world.add_collision_pairs(None, effect2, 'player:attack')
                    game_world.add_collision_pairs(None, effect3, 'player:attack')
                elif type(monster) == Enemy.Boss:
                    if monster.behavior == 'ATTACK_1':
                        effect = Effect.Boss_Attack_BloodWind(monster, Player, 1)
                        effect2 = Effect.Boss_Attack_BloodWind(monster, Player, -1)
                        game_world.add_object(effect, 4)
                        game_world.add_object(effect2, 4)
                        game_world.add_collision_pairs(None, effect, 'player:attack')
                        game_world.add_collision_pairs(None, effect2, 'player:attack')
                    elif monster.behavior == 'ATTACK_2':
                        effects = [Effect.Boss_Attack_SummonMiniBoss(monster, Player, 'up'),
                                   Effect.Boss_Attack_SummonMiniBoss(monster, Player, 'down'),
                                   Effect.Boss_Attack_SummonMiniBoss(monster, Player, 'right'),
                                   Effect.Boss_Attack_SummonMiniBoss(monster, Player, 'left')]
                        game_world.add_objects(effects, 4)
                        for effect in effects:
                            game_world.add_collision_pairs(None, effect, 'player:attack')
                    elif monster.behavior == 'ATTACK_3':
                        effects = [Effect.Boss_Attack_Needle(monster, Player,'right'),
                                   Effect.Boss_Attack_Needle(monster, Player,'right_up'),
                                   Effect.Boss_Attack_Needle(monster, Player,'up'),
                                   Effect.Boss_Attack_Needle(monster, Player,'left_up'),
                                   Effect.Boss_Attack_Needle(monster, Player,'left'),
                                   Effect.Boss_Attack_Needle(monster, Player,'left_down'),
                                   Effect.Boss_Attack_Needle(monster, Player,'down'),
                                   Effect.Boss_Attack_Needle(monster, Player,'right_down')]
                        game_world.add_objects(effects, 4)
                        for effect in effects:
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
        if not Fu_Va.phase_1:
            if len(game_world.objects[3]) == 0:
                game_world.add_object(Enemy.Boss(), 3)
                Fu_Va.phase_1 = True
                Fu_Va.phase_2 = True
        if Fu_Va.phase_2:
            if len(game_world.objects[3]) == 0:
                server.HP_Crystal = Object.HP_Crystal(400, 300, Player)  # Player ????????? ?????? Player ?????? ????????? ??????
                game_world.add_object(server.HP_Crystal, 1)
                server.Button_HP_Crystal = Interact(Player, server.HP_Crystal, 30)
                game_world.add_object(server.Button_HP_Crystal, 5)
                server.Portal_Up = Object.Portal('./Object/ETC/Portal_UP.png', 400, 507)
                game_world.add_object(server.Portal_Up, 1)

                Fu_Va.phase_2 = False




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
    server.Background = Castle_Stage()
    game_world.add_object(server.Background, 0)
    Fu_Va.select_Monster()  # ????????? ?????? (?????? ????????? add_object ?????? ??? ?????????)
    Fu_Va.phase_1 = server.phase_1
    Fu_Va.phase_2 = server.phase_2


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