from pico2d import *


class Shield:
    image = None
    x, y = None, None
    judge_click = False
    Player = None

    def act(self):  # 상호작용
        if self.judge_click:
            self.judge_click = False
        else:
            self.judge_click = True

    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
        self.equip()

    def equip(self):  # 상호작용 한 다음에는 착용했다는 표시로 오른쪽 아래에 그리기
        if self.judge_click:
            self.image.draw(775, 25)


class BlueShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_BlueShield.png')
        self.Player = Player

    def update(self):  # 공 5 증가
        if self.judge_click:
            self.Player.ATK = 15
        else:
            self.Player.ATK = 10

class RedcrossShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_RedCrossShield.png')
        self.Player = Player

    def update(self):  # 피 5 회복
        if self.judge_click:
            if self.Player.cur_name() == 'PARRYING':
                if not self.Player.hit:  # 1회만 회복되도록 처치 ( Player.check_hit 에서 .hit을 패링 시 False로 하고, 이 함수를 실행, Player.update에서 hit을 다시 None으로 조정함으로 반복가능~
                    if self.Player.HP < 95:
                        self.Player.HP += 10
                    elif self.Player.HP == 95:
                        self.Player.HP += 5

class CarShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_CarShield.png')
        self.Player = Player

    def update(self):  # 자동차 소환
        pass


class DragonShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_DragonShield.png')
        self.Player = Player

    def update(self):  # 전방에 브레스
        pass


class GukpongShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_GukPongShield.png')
        self.Player = Player

    def update(self):  # 발 밑에 태극문양(개사기버프)
        pass


class LockShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_LockShield.png')
        self.Player = Player

    def update(self):  # 적을 잠시 멈춤
        pass


class SoulShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_SoulShield.png')
        self.Player = Player

    def update(self):  # 스테이지당 한 번 강력한 빔 사출 가능
        pass


class ToyShield(Shield):
    def __init__(self, x, y, Player):
        self.x, self.y = x, y
        self.image = load_image('./Object/Shield/Shield_ToyShield.png')
        self.Player = Player

    def update(self):  # 발 밑에 지뢰(적이 밟으면 데미지)
        pass