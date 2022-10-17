from pico2d import *
import Player
import Background
import Handle_Event
import Object
import Enemy
import Interact
import Shield

open_canvas()
Backgrounds = Background.Background()
Player_Walk = Player.Player()
Player_Dash = Player.Player_Dash()
Player_Parrying = Player.Player_Parrying()
MonsterBox = Object.MonsterBox()
Test_Monster = Enemy.Test_Monster()
Effect = [Enemy.Test_Monster_Attack_Effect() for i in range(1)]
Button_MonsterBox = Interact.Interact()
num = 0
num2 = 1
Button_BlueShield = Interact.Interact()
Button_RedCrossShield = Interact.Interact()
Shields = [Shield.Shield() for a in range(2)]


def Button_RedCrossShield_Make():
    Button_RedCrossShield.set_xy(Player_Walk)
    Button_RedCrossShield.draw(Shields[1], 50)


def Button_BlueShield_Make():
    Button_BlueShield.set_xy(Player_Walk)
    Button_BlueShield.draw(Shields[0], 50)


def RedCrossShield_Use():
    Shields[1].attack(Player_Walk)
    Shields[1].Shield_ability()


def BlueShield_Use():
    Shields[0].attack(Player_Walk)
    Shields[0].Shield_ability()


def Shields_Make():
    for i in range(2):
        Shields[i].draw()
        Shields[i].equip()


def Test_Monster_Effect():
    global num, num2
    num2 = (num2 + 1) % 2
    for effect in Effect:
        effect.draw()
        effect.update()
        if len(Effect) == 6:
            Effect.pop(0)
    if Test_Monster.summon == 'on':
        if num2 == 0:
            if Test_Monster.frame == 3:
                Effect.append(Enemy.Test_Monster_Attack_Effect())
                Effect[len(Effect)-1].judge = 'on'


def Test_Monster_Summon():
    Test_Monster.draw()
    Test_Monster.update()
    Test_Monster_Effect()


def Button_MonsterBox_Make():
    Button_MonsterBox.set_xy(Player_Walk)
    Button_MonsterBox.draw(MonsterBox, 50)


def Dash():
    if Player_Walk.dash == 'on':
        Player_Dash.set_dir(Player_Walk)
        for a in range(4):
            clear_canvas()
            Backgrounds.draw()
            Player_Dash.draw()
            Button_MonsterBox_Make()
            MonsterBox.draw()
            Test_Monster_Summon()
            Button_BlueShield_Make()
            Button_RedCrossShield_Make()
            Shields_Make()
            update_canvas()
            Player_Dash.update(Player_Walk)
            delay(0.05)
        Player_Walk.dash = 'off'


def Parrying():
    if Player_Walk.parrying == 'on':
        Player_Parrying.set_exdir(Player_Walk)
        for a in range(9):
            clear_canvas()
            Backgrounds.draw()
            Player_Parrying.draw()
            Button_MonsterBox_Make()
            MonsterBox.draw()
            Test_Monster_Summon()
            Button_BlueShield_Make()
            Button_RedCrossShield_Make()
            Shields_Make()
            update_canvas()
            Player_Parrying.update()
            Player_Parrying.hit(Effect, BlueShield_Use, RedCrossShield_Use, Shields, Player_Walk)
            delay(0.05)

        Player_Walk.parrying = 'off'


def Walking():
    # 클리어
    clear_canvas()
    # 배경 그리기
    Backgrounds.draw()
    # 이동 그리기
    Player_Walk.draw()
    # 몬스터 박스 상호작용 키 그리기
    Button_MonsterBox_Make()
    # 몬스터 박스 그리기
    MonsterBox.draw()
    # 몬스터 박스 상호작용 시 나오는 몬스터
    Test_Monster_Summon()
    # 파란 방패 상호작용 키 그리기
    Button_BlueShield_Make()
    # 적십자 방패 상호작용 키 그리기
    Button_RedCrossShield_Make()
    # 방패 설치
    Shields_Make()
    # 캔버스 업데이트
    update_canvas()
    # 입력 받기
    Handle_Event.handle_events(Player_Walk, Button_MonsterBox, Button_BlueShield, Button_RedCrossShield, Test_Monster, Shields, Player_Parrying)
    # 대쉬
    Dash()
    # 패링
    Parrying()
    # 좌우 설정
    Player_Walk.set_exdir()
    # 걷기 업데이트
    Player_Walk.update()
    # 딜레이
    delay(0.05)


Shields[0].set_Shield('../Object/Shield/Shield_BlueShield.png')
Shields[0].set_xy(600, 400)
Shields[1].set_Shield('../Object/Shield/Shield_RedCrossShield.png')
Shields[1].set_xy(450, 400)
while Handle_Event.running:
    Walking()

close_canvas()
