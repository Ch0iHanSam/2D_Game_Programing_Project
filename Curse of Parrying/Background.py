from pico2d import *


class Test_Background:
    def __init__(self):
        self.image = load_image('./BackGround/Practice.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass

class Home_Stage:
    def __init__(self):
        self.image = load_image('./BackGround/Home_Stage.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


class Forest_Stage:
    def __init__(self):
        self.image = load_image('./BackGround/Forest_Stage.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


class Beach_Stage:
    def __init__(self):
        self.image = load_image('BackGround/Beach_Stage.png')
        self.frame = 0
        self.delay = get_time()

    def draw(self):
        self.image.clip_draw(self.frame*800, 0, 400, 300, 400, 300, 800, 600)

    def update(self):
        if get_time() - self.delay > 0.2:
            self.delay = get_time()
            self.frame = (self.frame + 1) % 6


class Castle_Stage:
    def __init__(self):
        self.image = load_image('./BackGround/Castle_Stage.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


class Pause:
    def __init__(self):
        self.image = load_image('./BackGround/Pause.png')

    def draw(self):
        self.image.draw(400,300)

    def update(self):
        pass

class Conversation:
    def __init__(self):
        self.image = load_image('./BackGround/conversation.png')

    def draw(self):
        self.image.draw(400,300)

    def update(self):
        pass