from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('../BackGround/Practice.png')
        self.x, self.y = 400, 300

    def draw(self):
        self.image.draw(self.x, self.y)


class Player:
    def __init__(self):
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 'idle'
        self.exdir = 'right'
        self.dash = 'off'

    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'up':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'down':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)



    def update(self):
        self.frame = (self.frame+1)%8
        if self.dir == 'right':
            self.x += 5
        elif self.dir == 'left':
            self.x -= 5
        elif self.dir == 'up':
            self.y += 5
        elif self.dir == 'down':
            self.y -= 5

    def set_exdir(self):
        if self.dir == 'right' or self.dir == 'left':
            self.exdir = self.dir

class Player_Dash:
    def __init__(self):
        self.image = load_image('../Object/Character/Dash/Character_Player_Dash.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir = ' '
        self.exdir = ' '


    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'up':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'down':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)


    def set_dir(self, Player):
        self.dir = Player.dir
        self.exdir = Player.exdir

    def update(self):
        if self.dir == 'right':
            self.x += 10
        elif self.dir == 'left':
            self.x -= 10
        elif self.dir == 'up':
            self.y += 10
        elif self.dir == 'down':
            self.y -= 10

def handle_events(Player, Player_Dash):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYUP and (event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_UP or event.key == SDLK_DOWN):
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

open_canvas()

running = True

Player = Player()
Background = Background()
Player_Dash = Player_Dash()

while running:
    clear_canvas()
    Background.draw()
    Player.draw()
    update_canvas()
    handle_events(Player, Player_Dash)
    if Player.dash == 'on':
        Player_Dash.set_dir(Player)
        for a in range(8):
            print('a')
            clear_canvas()
            Background.draw()
            Player_Dash.draw()
            update_canvas()
            Player_Dash.update()
            delay(0.01)
        Player.dash = 'off'
    while Player.dir != 'idle':
        clear_canvas()
        Background.draw()
        Player.draw()
        update_canvas()
        Player.set_exdir()
        handle_events(Player, Player_Dash)
        if Player.dash == 'on':
            Player_Dash.set_dir(Player)
            for a in range(8):
                print('a')
                clear_canvas()
                Background.draw()
                Player_Dash.draw()
                update_canvas()
                Player_Dash.update()
                delay(0.01)
            Player.dash = 'off'
        Player.update()
        delay(0.05)
    delay(0.05)

del Player
del Background

close_canvas()
