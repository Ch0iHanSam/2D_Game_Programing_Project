from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('../BackGround/Practice.png')

    def draw(self):
        self.image.draw(400,300)

class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 'idle_right'
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')

    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame*68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle_right':
            self.image.clip_draw(68*3, 100, 68, 68, self.x, self.y)
        elif self.dir == 'idle_left':
            self.image.clip_draw(68*3, 0, 68, 68, self.x, self.y)


    def update(self):
        self.frame = (self.frame+1)%8
        if self.dir == 'right':
            self.x += 5
        elif self.dir == 'left':
            self.x -= 5

def handle_events(Player):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False




open_canvas()

Background = Background()
Player = Player()

running = True

while running:
    clear_canvas()
    Background.draw()
    handle_events(Player)
    update_canvas()
    delay(0.07)

del Player
del Background

close_canvas()