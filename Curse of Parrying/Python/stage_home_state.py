from pico2d import *
import game_framework
import stage_lab_state
import pause_state
import stage_forest_state
from Player import Player_Character
from Background import Home_Stage
import Object
import Effect
from Interact import Interact
import server

class Fu_Va:
    running = True
    first_x, first_y = 400, 330

    @staticmethod
    def Portal_update():
        Portal_Right.update()
        Portal_Up.update()
        if Portal_Right.x + 24 < Player.x < Portal_Right.x + 48 and Portal_Right.y < Player.y < Portal_Right.y + 55:
            Portal_Up.check_enter(Player, stage_forest_state, -25, 25, 45, 85, 'stage_home', 'stage_1')
            Portal_Right.check_enter(Player, stage_lab_state, 24, 48, 0, 55,'stage_home', 'stage_lab')
        elif Portal_Up.x - 25 < Player.x < Portal_Up.x + 25 and Portal_Up.y + 45 < Player.y < Portal_Up.y + 85:
            Portal_Right.check_enter(Player, stage_lab_state, 24, 48, 0, 55, 'stage_home', 'stage_lab')
            Portal_Up.check_enter(Player, stage_forest_state, -25, 25, 45, 85, 'stage_home', 'stage_1')

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

    @staticmethod
    def Draw_Enter_Stage_1():
        enter_lab = load_image('../BackGround/Lab_Enter.png')
        if Portal_Up.out_stage_name() == 'stage_1':
            for i in range(14):
                clear_canvas()
                draw_world()
                enter_lab.clip_draw(i * 400, 0, 400, 300, 400, 300, 800, 600)
                update_canvas()
                delay(0.03)
            delay(0.5)


################### 생성되는 객체들 선언부 #####################################
Player = server.Player  # 플레이어
Background = Home_Stage  # 배경
Portal_Up = Object.Portal  # 위쪽 포탈
Portal_Right = Object.Portal  # 오른쪽 포탈
HP = Effect.HP  # 플레이어 HP
Pause = Effect.Pause  # 일시정지 버튼
Unknown = Object.Unknown  # 물음표 NPC
Button_Unknown = Interact # NPC 상호작용
############### enter에서 한번더 선언, exit에서 삭제###############################

def handle_events():
    if Fu_Va.running:
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):  # 상호작용
                Button_Unknown.handle_event(event)
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if 750 < event.x < 790 and 10 < event.y < 50:
                    game_framework.push_state(pause_state)
            else:
                Player.handle_event(event)  # 플레이어에게 이벤트를 전달함


def enter():
    Fu_Va.running = True
    global Player, Background, Portal_Up, Portal_Right, HP, Pause, Unknown, Button_Unknown
    Background = Home_Stage()
    Portal_Up = Object.Portal('../Object/ETC/Portal_UP.png', 400, 507)
    Portal_Right = Object.Portal('../Object/ETC/Portal_RIGHT.png', 703, 300)
    Unknown = Object.Unknown(450, 300)
    Button_Unknown = Interact()
    ########################아래 줄은 항상 마지막에(객체 추가 후 그려야됨)#################################
    # 인터페이스나 Player을 받아야 하는 객체를 여기에 쓰는 것임
    Pause = Effect.Pause()
    if game_framework.ex_state is None:
        server.Player = Player_Character(0, 0, 1)
        Player = server.Player
        Player.set_xy(Fu_Va.first_x, Fu_Va.first_y, 1)
        HP = Effect.HP(Player)
    elif game_framework.ex_state == stage_lab_state:
        Player = server.Player
        Player.set_xy(680, 330, -1)
        HP = Effect.HP(Player)
        Fu_Va.Draw_Enter_This_Stage()
    elif game_framework.ex_state == stage_forest_state:
        Player = server.Player
        Player.set_xy(400, 520, 1)
        HP = Effect.HP(Player)
        Fu_Va.Draw_Enter_This_Stage()



def exit():
    Fu_Va.running = False
    global Player, Background, Portal_Up, Portal_Right, HP, Pause, Unknown, Button_Unknown
    Fu_Va.Draw_Enter_Lab_Stage()
    Fu_Va.Draw_Enter_Stage_1()
    # del Player
    del Background
    del Portal_Up
    del Portal_Right
    del HP
    del Pause
    del Unknown
    del Button_Unknown


def update():
    if Fu_Va.running:
        Player.update()
        HP.update(Player)
        Button_Unknown.update(Player, Unknown)

        Fu_Va.Portal_update()# 포탈 업데이트는 항상 마지막에(exit하면서 다른 객체들이 삭제되기 때문에 이 밑에 다른 객체 update가 있으면 오류남)




def draw_world():
    Background.draw()
    Portal_Up.draw()
    Portal_Right.draw()
    Player.draw()
    Unknown.draw()
    Button_Unknown.draw(Unknown, 20)
    # 인터페이스들은 가장 위에 그려지게끔
    HP.draw()
    Pause.draw()


def draw():
    if Fu_Va.running:
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
