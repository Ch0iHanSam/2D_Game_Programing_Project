from pico2d import *

open_canvas()

character = load_image('../Object/Character/Walking/Character_Player_Walking.png')


def handle_events():
    global running
    global dir_x
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x = 400
y = 90
frame = 0
dir_x = 0
dir_y = 0
a = 0

while running:
    clear_canvas()
    character.clip_draw(frame*68, 0, 68, 68, x, y)
    update_canvas()
    handle_events()
    if a%5 == 0:
        frame = (frame +1)%8
    a += 1
    x += dir_x * 5
    y += dir_y * 5
    delay(0.01)

close_canvas()