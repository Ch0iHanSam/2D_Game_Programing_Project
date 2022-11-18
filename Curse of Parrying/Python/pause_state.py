from pico2d import *
import game_framework
from Background import Pause
import stage_home_state
import stage_lab_state


class Fu_Va:
    running = True



################### 생성되는 객체들 선언부 #####################################
Background = Pause  # 배경
############### enter에서 한번더 선언, exit에서 삭제###############################

def handle_events():
    if Fu_Va.running:
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                game_framework.pop_state()


def enter():
    Fu_Va.running = True
    global Background
    Background = Pause()



def exit():
    Fu_Va.running = False
    global Background
    del Background


def update():
    pass


def draw_world():
    if game_framework.stack[0] == stage_home_state:
        stage_home_state.draw_world()
    elif game_framework.stack[0] == stage_lab_state:
        stage_lab_state.draw_world()
    Background.draw()


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
