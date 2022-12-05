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