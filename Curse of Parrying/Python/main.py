from pico2d import *
import Player
import Background
import Handle_Event
import Object
import Enemy
import Interact

open_canvas()
Backgrounds = Background.Background()
Player_Walk = Player.Player()
Player_Dash = Player.Player_Dash()
Player_Parrying = Player.Player_Parrying()
MonsterBox = Object.MonsterBox()
Test_Monster = Enemy.Test_Monster()
Effect = [Enemy.Test_Monster_Attack_Effect() for i in range(1)]
Button_F = Interact.Interact()
num = 0
num2 = 1


def Test_Monster_Summon():
    global num, num2
    Test_Monster.draw()
    Test_Monster.update()
    if Test_Monster.summon == 'on':
        num2 = (num2 + 1)%2
        for effect in Effect:
            effect.draw()
            effect.update()
            if len(Effect) == 10:
                Effect.pop(0)
        if num2 == 0:
            if Test_Monster.frame == 3:
                Effect.append(Enemy.Test_Monster_Attack_Effect())
                Effect[num].judge = 'on'
                if num < 9:
                    num += 1


def Button_F_Make():
    Button_F.set_xy(Player_Walk)
    Button_F.draw(MonsterBox, 50)


def Dash():
    if Player_Walk.dash == 'on':
        Player_Dash.set_dir(Player_Walk)
        for a in range(4):
            clear_canvas()
            Backgrounds.draw()
            Player_Dash.draw()
            Button_F_Make()
            MonsterBox.draw()
            Test_Monster_Summon()
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
            Button_F_Make()
            MonsterBox.draw()
            Test_Monster_Summon()
            update_canvas()
            Player_Parrying.update()
            delay(0.05)
        Player_Walk.parrying = 'off'


def Walking():
    clear_canvas()
    Backgrounds.draw()
    Player_Walk.draw()
    Button_F_Make()
    MonsterBox.draw()
    Test_Monster_Summon()
    update_canvas()
    Handle_Event.handle_events(Player_Walk, Button_F, Test_Monster)
    Dash()
    Parrying()
    Player_Walk.set_exdir()
    Player_Walk.update()
    delay(0.05)


while Handle_Event.running:
    Walking()

close_canvas()
