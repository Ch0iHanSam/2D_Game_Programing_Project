from pico2d import *
import Player
import Handle_Event

open_canvas()
Player_Walk = Player.Player()
Player_Dash = Player.Player_Dash()
Player_Parrying = Player.Player_Parrying()


def Dash():
    if Player_Walk.dash == 'on':
        Player_Dash.set_dir(Player_Walk)
        for a in range(4):
            clear_canvas()
            Player_Dash.draw()
            update_canvas()
            Player_Dash.update(Player_Walk)
            delay(0.05)
        Player_Walk.dash = 'off'


def Parrying():
    if Player_Walk.parrying == 'on':
        Player_Parrying.set_exdir(Player_Walk)
        for a in range(9):
            clear_canvas()
            Player_Parrying.draw()
            update_canvas()
            Player_Parrying.update()
            delay(0.05)
        Player_Walk.parrying = 'off'


def Walking():
    clear_canvas()
    Player_Walk.draw()
    update_canvas()
    Handle_Event.handle_events(Player_Walk)
    Dash()
    Parrying()
    Player_Walk.set_exdir()
    Player_Walk.update()
    delay(0.05)


while Handle_Event.running:
    Walking()

close_canvas()
