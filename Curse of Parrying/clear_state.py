from pico2d import *
import game_framework
from Background import Clear

Background = Clear


def handle_events():
    events = get_events()
    for event in events:
        if event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()


def enter():
    global Background
    Background = Clear()

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
