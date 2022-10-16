from pico2d import *
import Player
import Handle_Event

open_canvas()
Player_Walk = Player.Player()
Player_Dash = Player.Player_Dash()
Player_Parrying = Player.Player_Parrying()


def Walking():
    clear_canvas()
    Player_Walk.draw()
    update_canvas()
    Handle_Event.handle_events(Player_Walk)
    Player_Walk.set_exdir()
    Player_Walk.update()
    delay(0.05)


def Dash():
    if Player_Walk.dash == 'on':
        Player_Dash


while Handle_Event.running:
    Walking()

close_canvas()
