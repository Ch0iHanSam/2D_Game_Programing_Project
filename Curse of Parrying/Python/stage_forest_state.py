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
import player_test
import server



class Fu_Va:
    running = True


    @staticmethod
    def Portal_Down_update():
        Portal_Down.update()
        Portal_Down.check_enter(Player, stage_home_state, -25, 25, -30, 2, 'stage_1', 'stage_home')


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
    def Draw_Enter_Home_Stage():
        enter_lab = load_image('../BackGround/Lab_Enter.png')  # 로딩창 다양하게 해서 수정해야함
        if Portal_Down.out_stage_name() == 'stage_home':
            for i in range(14):
                clear_canvas()
                draw_world()
                enter_lab.clip_draw(i * 400, 0, 400, 300, 400, 300, 800, 600)
                update_canvas()
                delay(0.03)
            delay(0.5)

    @staticmethod
    def update_Player():
        Player.update()
        # Player.check_hit(Test_Monster_Effect)  # 몬스터 소환한 뒤에 설정 다시 해줘야함

################### 생성되는 객체들 선언부 #####################################
Player = server.Player  # 플레이어
Background = Home_Stage  # 배경
Portal_Down = Object.Portal # 포탈
HP = Effect.HP  # 플레이어 HP
Pause = Effect.Pause  # 일시정지 버튼
############### enter에서 한번더 선언, exit에서 삭제###############################

def handle_events():
    if Fu_Va.running:
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
    Fu_Va.running = True
    global Player, Background, Portal_Down, HP, Pause
    Player = server.Player
    Player.set_xy(400, 120, 1)
    Background = Home_Stage()
    Portal_Down = Object.Portal('../Object/ETC/Portal_Down.png', 400, 95)
    # 인터페이스
    HP = Effect.HP(Player)
    Pause = Effect.Pause()
    # 마지막에 넣어야함
    Fu_Va.Draw_Enter_This_Stage()


def exit():
    Fu_Va.running = False
    global Player, Background, Portal_Down, HP, Pause
    Fu_Va.Draw_Enter_Home_Stage()
    del Player
    del Background
    del Portal_Down
    del HP
    del Pause


def update():
    if Fu_Va.running:
        Fu_Va.update_Player()
        HP.update(Player)

        Fu_Va.Portal_Down_update()  # 포탈 업데이트는 항상 마지막에(exit하면서 다른 객체들이 삭제되기 때문에 이 밑에 다른 객체 update가 있으면 오류남)


def draw_world():
    Background.draw()
    Portal_Down.draw()
    Player.draw()

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
    import stage_forest_state

    pico2d.open_canvas()
    game_framework.run(stage_1_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()