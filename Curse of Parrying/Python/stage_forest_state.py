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
    def Portal_Down_update():
        server.Portal_Down.check_enter(Player, stage_home_state, -25, 25, -30, 2)

    @staticmethod
    def update_Player():
        Player.update()
        # Player.check_hit(Test_Monster_Effect)  # 몬스터 소환한 뒤에 설정 다시 해줘야함


Player = None  # 플레이어


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):  # 일시정지
            if 750 < event.x < 790 and 10 < event.y < 50:
                game_framework.push_state(pause_state)
        else:
            Player.handle_event(event)  # 플레이어에게 이벤트를 전달함


def enter():
    global Player
    Player = server.Player
    Player.set_xy(400, 120, 1)
    game_world.add_object(Player, 1)
    server.Background = Home_Stage()
    game_world.add_object(server.Background, 0)
    server.Portal_Down = Object.Portal('../Object/ETC/Portal_Down.png', 400, 95)
    game_world.add_object(server.Portal_Down, 1)
    server.Monsters = [Enemy.Pigeon(7) for i in range(10)]
    game_world.add_objects(server.Monsters, 3)

    # 인터페이스
    server.HP = Effect.HP(Player)
    game_world.add_object(server.HP, 6)
    server.Pause = Effect.Pause()
    game_world.add_object(server.Pause, 6)



def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    Fu_Va.Portal_Down_update()  # 포탈 업데이트는 항상 마지막에(exit하면서 다른 객체들이 삭제되기 때문에 이 밑에 다른 객체 update가 있으면 오류남)


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
    import stage_forest_state

    pico2d.open_canvas()
    game_framework.run(stage_forest_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()