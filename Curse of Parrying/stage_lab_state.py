from pico2d import *
import game_framework
import stage_home_state
import pause_state
from Player import Player_Character
from Background import Home_Stage
import Object
import Enemy
from Interact import Interact
import Shield
import Effect
import server
import game_world


class Fu_Va:

    @staticmethod
    def Portal_Left_update():
        server.Portal_Left.check_enter(Player, stage_home_state, -50, -20, 0, 57)


    @staticmethod
    def monster_attack_effect():
        if server.Test_Monster.attack:
            effect = Effect.Test_Monster_Effect(server.Test_Monster.x + 30, server.Test_Monster.y, server.Test_Monster)
            game_world.add_object(effect, 4)
            game_world.add_collision_pairs(None, effect, 'player:attack')
        for i in game_world.objects[4]:
            if i.x > 600:
                game_world.remove_object(i)

    @staticmethod
    def handle_event_Button(event):
        for i in game_world.objects[5]:
            i.handle_event(event)

    @staticmethod
    def collide(a, b):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        return True


Player = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):  # 상호작용
            Fu_Va.handle_event_Button(event)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 750 < event.x < 790 and 10 < event.y < 50:
                game_framework.push_state(pause_state)
        else:
            Player.handle_event(event)  # 플레이어에게 이벤트를 전달함


def enter():
    global Player
    Player = server.Player
    Player.set_xy(120, 330, 1)
    game_world.add_object(Player, 1)
    server.Background = Home_Stage()
    game_world.add_object(server.Background, 0)
    server.Portal_Left = Object.Portal('./Object/ETC/Portal_LEFT.png', 97, 300)
    game_world.add_object(server.Portal_Left, 1)
    server.Test_Monster = Enemy.Test_Monster()
    game_world.add_object(server.Test_Monster, 3)
    server.Monster_Box = Object.Test_Monster_Box(400, 450, server.Test_Monster)  # 몬스터를 받아야하기 때문에 항상 몬스터 뒤에 위치
    game_world.add_object(server.Monster_Box, 1)
    server.Button_MonsterBox = Interact(Player, server.Monster_Box, 20)  # 몬스터박스 밑에
    game_world.add_object(server.Button_MonsterBox, 5)
    # 0 : 파랑방패, 1 : 회복방패, 2 : 어디서많이본방패, 3 : 드래곤실드, 4 : 우리의 것, 5 : 자물쇠방패, 6 : 소울실드, 7 : 장난감방패
    server.Shields = [Shield.BlueShield(100, 520, Player), Shield.RedcrossShield(160, 520, Player),
                      Shield.CarShield(220, 520, Player), Shield.DragonShield(280, 520, Player),
                      Shield.GukpongShield(340, 520, Player), Shield.LockShield(400, 520, Player),
                      Shield.SoulShield(460, 520, Player), Shield.ToyShield(520, 520, Player)]
    game_world.add_objects(server.Shields, 2)
    server.Button_Shield = [Interact(Player, server.Shields[0], 20), Interact(Player, server.Shields[1], 20),
                            Interact(Player, server.Shields[2], 20), Interact(Player, server.Shields[3], 20),
                            Interact(Player, server.Shields[4], 20), Interact(Player, server.Shields[5], 20),
                            Interact(Player, server.Shields[6], 20), Interact(Player, server.Shields[7], 20)]
    game_world.add_objects(server.Button_Shield, 5)
    server.HP = Effect.HP(Player)
    game_world.add_object(server.HP, 6)
    server.Pause = Effect.Pause()
    game_world.add_object(server.Pause, 6)


    #충돌 처리
    game_world.add_collision_pairs( Player, None, 'player:attack')


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if Fu_Va.collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    Fu_Va.Portal_Left_update()  # 포탈 업데이트는 항상 마지막에(exit하면서 다른 객체들이 삭제되기 때문에 이 밑에 다른 객체 update가 있으면 오류남)


def draw_world():
    Fu_Va.monster_attack_effect()  # 몬스터 공격 이펙트 생성/제거 함수

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


# 게임 실행
def test_self():
    import stage_lab_state

    pico2d.open_canvas()
    game_framework.run(stage_lab_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()