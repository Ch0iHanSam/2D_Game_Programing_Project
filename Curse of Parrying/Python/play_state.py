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
Player_Parrying = Player.Player_Parrying()
MonsterBox = Object.MonsterBox()
Test_Monster = Enemy.Test_Monster()
Effect = [Enemy.Test_Monster_Attack_Effect() for i in range(1)]
Button_MonsterBox = Interact.Interact()
Button_BlueShield = Interact.Interact()
Button_RedCrossShield = Interact.Interact()
Shields = [Shield.Shield() for a in range(2)]
effect_judge = False


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


# 테스트 몬스터 공격 그리기
def Test_Monster_Effect():
    global effect_judge
    for effect in Effect:
        effect.draw()
        effect.update()
    if Test_Monster.summon == 'on':
        if Test_Monster.frame == 3:
            Test_Monster.frame += 1
            if effect_judge:
                effect_judge = False
            elif not effect_judge:
                effect_judge = True
            if effect_judge:
                Effect.append(Enemy.Test_Monster_Attack_Effect())
                Effect[len(Effect) - 1].judge = 'on'


# 테스트 몬스터 그리기, 몬스터 공격 발사
def Test_Monster_Summon():
    Test_Monster.draw()
    Test_Monster.update()
    Test_Monster_Effect()


# 몬스터 박스 설치
def Button_MonsterBox_Make():
    Button_MonsterBox.set_xy(Player_Walk)
    Button_MonsterBox.draw(MonsterBox, 50)


def Parrying():
    if Player_Walk.parrying:
        Player_Parrying.set_exdir(Player_Walk)
        while Player_Parrying.do == True:
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
            delay(0.01)
        Player_Walk.parrying = False


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
    Handle_Event.handle_events(Player_Walk, Button_MonsterBox, Button_BlueShield, Button_RedCrossShield, Test_Monster,
                               Shields, Player_Parrying)
    # 패링
    Parrying()
    # 좌우 설정
    Player_Walk.set_exdir()
    # 걷기 업데이트
    Player_Walk.update()
    # 딜레이
    delay(0.01)


Shields[0].set_Shield('../Object/Shield/Shield_BlueShield.png')
Shields[0].set_xy(600, 400)
Shields[1].set_Shield('../Object/Shield/Shield_RedCrossShield.png')
Shields[1].set_xy(450, 400)


def Run():
    while Handle_Event.running:
        Walking()

    close_canvas()
