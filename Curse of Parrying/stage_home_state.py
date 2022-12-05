from pico2d import *
import game_framework
import stage_lab_state
import pause_state
import stage_forest_state
import stage_beach_state
from Player import Player_Character
from Background import Home_Stage
import Object
import Effect
from Interact import Interact
import server
import game_world

class Fu_Va:
    first_x, first_y = 400, 330

    @staticmethod
    def Portal_update():
        if server.Portal_Right.x + 24 < server.Player.x < server.Portal_Right.x + 48 and server.Portal_Right.y < server.Player.y < server.Portal_Right.y + 55:
            server.Portal_Up.check_enter(server.Player, stage_forest_state, -25, 25, 45, 85)
            server.Portal_Right.check_enter(server.Player, stage_lab_state, 24, 48, 0, 55)
        elif server.Portal_Up.x - 25 < server.Player.x < server.Portal_Up.x + 25 and server.Portal_Up.y + 45 < server.Player.y < server.Portal_Up.y + 85:
            server.Portal_Right.check_enter(server.Player, stage_lab_state, 24, 48, 0, 55)
            server.Portal_Up.check_enter(server.Player, stage_forest_state, -25, 25, 45, 85)


Player = None  # 플레이어



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):  # 상호작용
            server.Button_Unknown.handle_event(event)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 750 < event.x < 790 and 10 < event.y < 50:
                game_framework.push_state(pause_state)
        else:
            Player.handle_event(event)  # 플레이어에게 이벤트를 전달함


def enter():
    global Player
    server.Background = Home_Stage()
    game_world.add_object(server.Background, 0)
    server.Portal_Up = Object.Portal('./Object/ETC/Portal_UP.png', 400, 507)
    game_world.add_object(server.Portal_Up, 1)
    server.Portal_Right = Object.Portal('./Object/ETC/Portal_RIGHT.png', 703, 300)
    game_world.add_object(server.Portal_Right, 1)
    server.Unknown = Object.Unknown(450, 300)
    game_world.add_object(server.Unknown, 1)
    ########################아래 줄은 항상 마지막에(객체 추가 후 그려야됨)#################################
    # 인터페이스나 Player을 받아야 하는 객체를 여기에 쓰는 것임
    server.Pause = Effect.Pause()
    game_world.add_object(server.Pause, 6)
    if game_framework.ex_state is None:
        server.Player = Player_Character(0, 0, 1)
        server.Player.set_xy(Fu_Va.first_x, Fu_Va.first_y, 1)
        Player = server.Player  # 플레이어는 자신의 정보를 그대로 가지고 있어야 하기 때문에 복사본을 넣어준다.
        game_world.add_object(Player, 1)
        server.Button_Unknown = Interact(Player, server.Unknown, 20)
        game_world.add_object(server.Button_Unknown, 5)
        server.HP = Effect.HP(Player)
        game_world.add_object(server.HP, 6)
    elif game_framework.ex_state == stage_lab_state:
        server.Player.set_xy(680, 330, -1)
        Player = server.Player
        game_world.add_object(Player, 1)
        server.Button_Unknown = Interact(Player, server.Unknown, 20)
        game_world.add_object(server.Button_Unknown, 5)
        server.HP = Effect.HP(Player)
        game_world.add_object(server.HP, 6)
    elif game_framework.ex_state == stage_forest_state:
        server.Player.set_xy(400, 520, 1)
        Player = server.Player
        game_world.add_object(Player, 1)
        server.Button_Unknown = Interact(Player, server.Unknown, 20)
        game_world.add_object(server.Button_Unknown, 5)
        server.HP = Effect.HP(Player)
        game_world.add_object(server.HP, 6)
    elif game_framework.ex_state == stage_beach_state:
        server.Player.set_xy(400, 120, 1)
        Player = server.Player
        game_world.add_object(Player, 1)
        server.Button_Unknown = Interact(Player, server.Unknown, 20)
        game_world.add_object(server.Button_Unknown, 5)
        server.HP = Effect.HP(Player)
        game_world.add_object(server.HP, 6)



def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    Fu_Va.Portal_update()# 포탈 체크는 항상 마지막에(exit하면서 다른 객체들이 삭제되기 때문에 이 밑에 다른 객체 update가 있으면 오류남)




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


# 게임 실행
def test_self():
    import stage_home_state

    pico2d.open_canvas()
    game_framework.run(stage_home_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()