from pico2d import *
import game_framework
import stage_lab_state
# import Player
# import Background
from Player import Player_Character
from Background import Home_Stage
import Handle_Event
import Object
import Enemy
import Interact
import Shield
import random


class Fu_Va:
    first_x, first_y = 400, 330
    first_judge = True
    first_enter = True

    @staticmethod
    def Portal_Right_update():
        Portal_Right.update()
        Portal_Right.check_enter(Player, stage_lab_state, 24, 48, 0, 55,'stage_home', 'stage_lab')

    @staticmethod
    def Draw_Enter_This_Stage():
        enter_lab = load_image('../BackGround/Lab_Enter_2.png')
        for i in range(11):
            clear_canvas()
            draw_world()
            enter_lab.clip_draw(i*400, 0, 400, 300, 400, 300, 800, 600)
            update_canvas()
            delay(0.03)

    @staticmethod
    def Draw_Enter_Lab_Stage():
        enter_lab = load_image('../BackGround/Lab_Enter.png')
        if Portal_Right.out_stage_name() == 'stage_lab':
            for i in range(14):
                clear_canvas()
                draw_world()
                enter_lab.clip_draw(i * 400, 0, 400, 300, 400, 300, 800, 600)
                update_canvas()
                delay(0.03)
            delay(0.5)


################### 생성되는 객체들 선언부 #####################################
Player = Player_Character  # 플레이어
Background = Home_Stage  # 배경
Portal_Up = Object.Portal  # 위쪽 포탈
Portal_Right = Object.Portal  # 오른쪽 포탈
############### enter에서 한번더 선언, exit에서 삭제###############################

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            Player.handle_event(event)  # 플레이어에게 이벤트를 전달함


def enter():
    global Player, Background, Portal_Up, Portal_Right
    Background = Home_Stage()
    Portal_Up = Object.Portal('../Object/ETC/Portal_UP.png', 400, 507)
    Portal_Right = Object.Portal('../Object/ETC/Portal_RIGHT.png', 703, 300)
    ########################아래 6줄은 항상 마지막에(객체 추가 후 그려야됨)#################################
    if Fu_Va.first_judge:
        Player = Player_Character(Fu_Va.first_x, Fu_Va.first_y, 1)
        Fu_Va.first_judge = False
    else:
        Player = Player_Character(680, 330, -1)
        Fu_Va.Draw_Enter_This_Stage()



def exit():
    global Player, Background, Portal_Up, Portal_Right
    Fu_Va.Draw_Enter_Lab_Stage()
    del Player
    del Background
    del Portal_Up
    del Portal_Right


def update():
    Player.update()
    Portal_Up.update()
    Fu_Va.Portal_Right_update()


def draw_world():
    Background.draw()
    Portal_Up.draw()
    Portal_Right.draw()
    Player.draw()


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
