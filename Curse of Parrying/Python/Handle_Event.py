from pico2d import *


running = True
def handle_events(Player):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYUP and (
                event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_UP or event.key == SDLK_DOWN):
            Player.dir = 'idle'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            Player.dir = 'right'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            Player.dir = 'left'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            Player.dir = 'up'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            Player.dir = 'down'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            Player.dash = 'on'
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            Player.parrying = 'on'