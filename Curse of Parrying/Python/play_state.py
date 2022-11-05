from pico2d import *
import game_framework
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

# open_canvas()
# # 배경
# Test_Background = Background.Test_Background()  # 배경
# Home_Stage = Background.Home_Stage()
# # 플레이어 움직임
# Player_Walk = Player.Player()  # 플레이어 걷기
# Player_Parrying = Player.Player_Parrying()  # 패링
# # 오브젝트
# MonsterBox = Object.MonsterBox()  # 몬스터박스(테스트 몬스터 소환)
# MonsterBox2 = Object.MonsterBox2()  # 몬스터박스2(몬스터 랜덤 배치)
# # 몬스터
# Test_Monster = Enemy.Test_Monster()  # 테스트 몬스터
# Monsters = []  # 몬스터들
# # 몬스터 공격
# Effect = [Enemy.Test_Monster_Attack_Effect(Test_Monster) for i in range(1)]
# # 상호작용 버튼
# Button_MonsterBox = Interact.Interact()
# Button_MonsterBox2 = Interact.Interact()
# Button_BlueShield = Interact.Interact()
# Button_RedCrossShield = Interact.Interact()
# # 방패
# Shields = [Shield.Shield() for a in range(2)]
# # 이펙트
# MagicCircle_Summon = [] #소환 마법진
# # 기타 변수
# effect_judge = False
# num_monster = 0
# enemy_variable = Enemy.Variable()
#
#
# # 몬스터 랜덤 저장
# def Random_Monster_Select():
#     global num_monster
#     Monsters.clear()
#     num_monster = random.randint(2, 20)
#     for i in range(num_monster):
#         monster_type = random.randint(1, 3)
#         if monster_type == 1:
#             Monsters.append(Enemy.Boar())
#         elif monster_type == 2:
#             Monsters.append(Enemy.Rabbit())
#         elif monster_type == 3:
#             Monsters.append(Enemy.Pigeon())
#
#
# # 몬스터 랜덤 위치 결정
# def Random_Monster_set_xy():
#     global num_monster
#     for i in range(num_monster):
#         Monsters[i].set_xy()
#         # 몬스터 위치 결정
#         for a in range(num_monster):
#             if i != a:
#                 while Monsters[a].x - 20 < Monsters[i].x < Monsters[a].x + 20 or Monsters[a].y - 20 < Monsters[i].y < Monsters[a].y + 20:
#                     Monsters[i].set_xy()
#
#
# # 몬스터 소환
# def Random_Monster_Summon():
#     for i in Monsters:
#         i.draw()
#         i.update()
#
#
# # 몬스터 소환 마법진
# def Magic_Circle_Monster_Summon():
#     global num_monster
#     for i in range(num_monster):
#         MagicCircle_Summon.append(Enemy.Summon())
#         MagicCircle_Summon[i].set_xy(Monsters[i])
#
#
# # 몬스터 소환 마법진 그리기
# def Magic_Circle_Monster_Summon_Draw():
#     for i in MagicCircle_Summon:
#         i.draw()
#         i.update()
#
#
# # 랜덤 몬스터 소환 전 과정
# def Monster_Summon():
#     if enemy_variable.monster_judge:
#         Random_Monster_Select()
#         Random_Monster_set_xy()
#         Magic_Circle_Monster_Summon()
#         enemy_variable.monster_judge = False
#         enemy_variable.magic_circle_summon_judge = True
#     if enemy_variable.magic_circle_summon_judge:
#         Magic_Circle_Monster_Summon_Draw()
#         if MagicCircle_Summon[0].frame == 16:
#             enemy_variable.magic_circle_summon_judge = False
#             for i in MagicCircle_Summon:
#                 i.frame = 1
#             enemy_variable.monster_summon = True
#     if enemy_variable.monster_summon:
#         Random_Monster_Summon()
#
#
# # 적십자방패 상호작용 버튼
# def Button_RedCrossShield_Make():
#     Button_RedCrossShield.set_xy(Player_Walk)
#     Button_RedCrossShield.draw(Shields[1], 50)
#
#
# # 파랑방패 상호작용 버튼
# def Button_BlueShield_Make():
#     Button_BlueShield.set_xy(Player_Walk)
#     Button_BlueShield.draw(Shields[0], 50)
#
#
# # 적십자 방패 사용
# def RedCrossShield_Use():
#     Shields[1].attack()
#     Shields[1].Shield_ability(Player_Walk)
#
#
# # 파랑 방패 사용
# def BlueShield_Use():
#     Shields[0].attack()
#     Shields[0].Shield_ability(Player_Walk)
#
#
# # 방패들 설치
# def Shields_Make():
#     for i in range(2):
#         Shields[i].draw()
#         Shields[i].equip()
#
#
# # 테스트 몬스터 공격 그리기
# def Test_Monster_Effect():
#     global effect_judge
#
#     for effect in Effect:
#         effect.draw()
#         effect.update(Effect)
#         effect.check_pop(Effect)
#     if Test_Monster.summon:
#         if Test_Monster.frame == 3:
#             Test_Monster.frame += 1
#             if effect_judge:
#                 effect_judge = False
#             elif not effect_judge:
#                 effect_judge = True
#             if effect_judge:
#                 Effect.append(Enemy.Test_Monster_Attack_Effect(Test_Monster))
#                 Effect[len(Effect) - 1].judge = True
#
#
# # 테스트 몬스터 그리기, 몬스터 공격 발사
# def Test_Monster_Summon():
#     Test_Monster.draw()
#     Test_Monster.update()
#     Test_Monster_Effect()
#
#
# # 몬스터박스 상호작용
# def Button_MonsterBox_Make():
#     Button_MonsterBox.set_xy(Player_Walk)
#     Button_MonsterBox.draw(MonsterBox, 35)
#
#
# # 몬스터박스2 상호작용
# def Button_MonsterBox2_Make():
#     Button_MonsterBox2.set_xy(Player_Walk)
#     Button_MonsterBox2.draw(MonsterBox2, 35)
#
#
# # 패링
# def Parrying():
#     if Player_Parrying.do:
#         Player_Parrying.set_exdir(Player_Walk)
#         while Player_Parrying.do:
#             clear_canvas()
#             Home_Stage.draw()
#             Player_Parrying.draw()
#             Monster_Summon()
#             Button_MonsterBox_Make()
#             Button_MonsterBox2_Make()
#             MonsterBox.draw()
#             MonsterBox2.draw()
#             Test_Monster_Summon()
#             Button_BlueShield_Make()
#             Button_RedCrossShield_Make()
#             Shields_Make()
#             update_canvas()
#             Player_Parrying.update()
#             Player_Parrying.hit(Effect, BlueShield_Use, RedCrossShield_Use, Player_Walk)
#             delay(0.01)
#
#
# # 걷기(게임 진행)
# def Walking():
#     # 클리어
#     clear_canvas()
#     # 배경 그리기
#     Home_Stage.draw()
#     # 이동 그리기
#     Player_Walk.draw()
#     # 몬스터 박스2 상호작용 시 나오는 몬스터
#     Monster_Summon()
#     # 몬스터 박스 상호작용 키 그리기
#     Button_MonsterBox_Make()
#     # 몬스터 박스2 상호작용 키 그리기
#     Button_MonsterBox2_Make()
#     # 몬스터 박스 그리기
#     MonsterBox.draw()
#     # 몬스터 박스2 그리기
#     MonsterBox2.draw()
#     # 몬스터 박스 상호작용 시 나오는 몬스터
#     Test_Monster_Summon()
#     # 파란 방패 상호작용 키 그리기
#     Button_BlueShield_Make()
#     # 적십자 방패 상호작용 키 그리기
#     Button_RedCrossShield_Make()
#     # 방패 설치
#     Shields_Make()
#     # 캔버스 업데이트
#     update_canvas()
#     # 입력 받기
#     Handle_Event.handle_events(Player_Walk, Button_MonsterBox, Button_MonsterBox2, Button_BlueShield,
#                                Button_RedCrossShield, Test_Monster, Shields, Player_Parrying, Monsters, enemy_variable)
#     # 패링
#     Parrying()
#     # 좌우 설정
#     Player_Walk.set_exdir()
#     # 걷기 업데이트
#     Player_Walk.update()
#     # 피격 체크
#     Player_Walk.check_hit(Effect)
#     # 딜레이
#     delay(0.01)
#
#
# # 방패 세팅
# Shields[0].set_Shield('../Object/Shield/Shield_BlueShield.png')
# Shields[0].set_xy(600, 400)
# Shields[1].set_Shield('../Object/Shield/Shield_RedCrossShield.png')
# Shields[1].set_xy(450, 400)
#
# def Run():
#     while Handle_Event.running:
#         Walking()
#
#     close_canvas()

Player = Player_Character  # 플레이어
Background = Home_Stage  # 배경

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
    global Player, Background
    Player = Player_Character()
    Background = Home_Stage()


def exit():
    global Player, Background
    del Player
    del Background


def update():
    Player.update()

def draw_world():
    Background.draw()
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
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
