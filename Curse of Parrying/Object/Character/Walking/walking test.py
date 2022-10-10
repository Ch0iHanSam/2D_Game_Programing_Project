from pico2d import *

running = True
x = 400
y = 90

def handle_events():
    global x
    global running
    
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running=False
            
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x += 5

character = load_image('Character_Player_Walking_sheet.png')

open_canvas()

frame = 0

while running:
    character.clip_draw(frame*68, 0, 0, 68, 68, 400+x, 90)

    update_canvas()
    handle_events()

    frame = (frame +1)%8

close_canvas()
    
