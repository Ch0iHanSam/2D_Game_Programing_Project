from pico2d import *
import game_framework
import stage_home_state
from Player import Player_Character
from Background import Home_Stage
import Object
import Enemy
from Interact import Interact
import Shield



class Fu_Va:
    running = True
    first_x, first_y = 400, 330
    first_judge = False


    @staticmethod
    def Portal_Left_update():
        Portal_Left.update()
        Portal_Left.check_enter(Player, stage_home_state, -50, -20, 0, 57, 'stage_lab', 'stage_home')


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
        enter_lab = load_image('../BackGround/Lab_Enter.png')
        if Portal_Left.out_stage_name() == 'stage_home':
            for i in range(14):
                clear_canvas()
                draw_world()
                enter_lab.clip_draw(i * 400, 0, 400, 300, 400, 300, 800, 600)
                update_canvas()
                delay(0.03)
            delay(0.5)

    @staticmethod
    def update_monster_effect():
        for i in Test_Monster_Effect:
            i.set_xy(Test_Monster)
            i.update()

    @staticmethod
    def draw_monster_effect():
        if Test_Monster.attack:
            Test_Monster_Effect.append(Enemy.Test_Monster_Effect())
        if Test_Monster_Effect:
            for i in Test_Monster_Effect:
                if i.x > 600:
                    Test_Monster_Effect.remove(i)
                i.draw()

    @staticmethod
    def update_Player():
        Player.update()
        Player.check_hit(Test_Monster_Effect)

    @staticmethod
    def draw_Shield():
        for i in Shields:
            i.draw()

    @staticmethod
    def update_Shield():
        for i in Shields:
            i.update(Player)

    @staticmethod
    def draw_Button_Shield():
        for i in range(8):
            Button_Shield[i].draw(Shields[i], 20)

    @staticmethod
    def update_Button_Shield():
        for i in range(8):
            Button_Shield[i].update(Player, Shields[i])

    @staticmethod
    def handle_event_Button_Shield(event):
        for i in Button_Shield:
            i.handle_event(event)

################### 생성되는 객체들 선언부 #####################################
Player = Player_Character  # 플레이어
Background = Home_Stage  # 배경
Portal_Left = Object.Portal  # 오른쪽 포탈
Monster_Box = Object.Test_Monster_Box  # 테스트 몬스터 소환 오브젝트
Button_MonsterBox = Interact  # 몬스터 박스 상호작용
Test_Monster = Enemy.Test_Monster  # 테스트 몬스터
Test_Monster_Effect = Enemy.Test_Monster_Effect  # 테스트 몬스터의 공격 이펙트
Shields = Shield.Shield  # 방패들
Button_Shield = Interact  # 방패 상호작용

############### enter에서 한번더 선언, exit에서 삭제###############################

def handle_events():
    if Fu_Va.running:
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):
                Button_MonsterBox.handle_event(event)
                Fu_Va.handle_event_Button_Shield(event)
            else:
                Player.handle_event(event)  # 플레이어에게 이벤트를 전달함


def enter():
    Fu_Va.running = True
    global Player, Background, Portal_Left, Monster_Box, Button_MonsterBox, Test_Monster, Test_Monster_Effect, Shields, Button_Shield
    if Fu_Va.first_judge:
        Player = Player_Character(Fu_Va.first_x, Fu_Va.first_y, 1)
    else:
        Player = Player_Character(120, 330, 1)
    Background = Home_Stage()
    Portal_Left = Object.Portal('../Object/ETC/Portal_LEFT.png', 97, 300)
    Button_MonsterBox = Interact()
    Test_Monster = Enemy.Test_Monster()
    Monster_Box = Object.Test_Monster_Box(400, 450, Test_Monster)  # 몬스터를 받아야하기 때문에 항상 몬스터 뒤에 위치
    Test_Monster_Effect = []
    # 0 : 파랑방패, 1 : 회복방패, 2 : 어디서많이본방패, 3 : 드래곤실드, 4 : 우리의 것, 5 : 자물쇠방패, 6 : 소울실드, 7 : 장난감방패
    Shields = [Shield.Shield(100, 520, '../Object/Shield/Shield_BlueShield.png'), Shield.Shield(160, 520, '../Object/Shield/Shield_RedCrossShield.png'),
               Shield.Shield(220, 520, '../Object/Shield/Shield_CarShield.png'), Shield.Shield(280, 520, '../Object/Shield/Shield_DragonShield.png'),
               Shield.Shield(340, 520, '../Object/Shield/Shield_GukPongShield.png'), Shield.Shield(400, 520, '../Object/Shield/Shield_LockShield.png'),
               Shield.Shield(460, 520, '../Object/Shield/Shield_SoulShield.png'), Shield.Shield(520, 520, '../Object/Shield/Shield_ToyShield.png')]
    Button_Shield = [Interact() for i in range(8)]
    ########################아래 6줄은 항상 마지막에(객체 추가 후 그려야됨)#################################
    Fu_Va.Draw_Enter_This_Stage()


def exit():
    Fu_Va.running = False
    global Player, Background, Portal_Left, Monster_Box, Button_MonsterBox, Test_Monster, Test_Monster_Effect, Shields, Button_Shield
    Fu_Va.Draw_Enter_Home_Stage()
    del Player
    del Background
    del Portal_Left
    del Monster_Box
    del Button_MonsterBox
    del Test_Monster
    del Test_Monster_Effect
    del Shields
    del Button_Shield


def update():
    if Fu_Va.running:
        Fu_Va.update_Player()
        Button_MonsterBox.update(Player, Monster_Box)
        Test_Monster.update()
        Fu_Va.update_monster_effect()
        Fu_Va.update_Shield()
        Fu_Va.update_Button_Shield()
        Fu_Va.Portal_Left_update()  # 포탈 업데이트는 항상 마지막에(exit하면서 다른 객체들이 삭제되기 때문에 이 밑에 다른 객체 update가 있으면 오류남)


def draw_world():
    Background.draw()
    Portal_Left.draw()
    Monster_Box.draw()
    Button_MonsterBox.draw(Monster_Box, 30)
    Test_Monster.draw()
    Fu_Va.draw_monster_effect()
    Fu_Va.draw_Shield()
    Player.draw()
    Fu_Va.draw_Button_Shield()


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
    import stage_lab_state

    pico2d.open_canvas()
    game_framework.run(stage_lab_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()