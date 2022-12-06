from pico2d import *
import game_framework
from Background import Death
import stage_home_state

Background = Death


def handle_events():
    events = get_events()
    for event in events:
        if event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):
                game_framework.change_state(stage_home_state)


def enter():
    global Background
    Background = Death()

def exit():
    global Background
    del Background

def update():
    pass

def draw_world():
    Background.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.01)

def pause():
    pass

def resume():
    pass
