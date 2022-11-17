from pico2d import *


class Shield:
    def __init__(self, x = 0, y = 0, image = None):
        self.image = load_image(image)
        self.name = image
        self.x, self.y = x, y
        self.judge_attack = False
        self.judge_click = False

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def equip(self):
        if self.judge_click:
            self.image.draw(750, 50)

    def draw(self):
        if self.image is not None:
            self.image.draw(self.x, self.y, 50, 50)
            self.equip()

    def attack(self):
        if self.judge_click:
            self.judge_attack = True

    def Shield_ability(self, Player):
        if self.judge_click:
            if self.name == '../Object/Shield/Shield_BlueShield.png':  # 파랑방패 - 공격력 5 증가
                Player.ATK += 5
            elif self.name == '../Object/Shield/Shield_RedCrossShield.png':  # 적십자방패 - 반격 시 HP 10 회복
                if self.judge_attack:
                    Player.hp += 10
                    print(Player.hp)
            elif self.name == '../Object/Shield/Shield_CarShield.png':  # 어디서 많이 본 방패 - 자동차 소환 (투사체 삭제, 데미지)
                pass
            elif self.name == '../Object/Shield/Shield_DragonShield.png':  # 드래곤실드 - 전방에 브레스
                pass
            elif self.name == '../Object/Shield/Shield_GukPongShield.png':  # 우리 것 - 발 밑에 태극문양, 버프(개지리는) -> 살짝 치트템?
                pass
            elif self.name == '../Object/Shield/Shield_LockShield.png':  # 자물쇠 방패 - 적을 잠시 멈춤
                pass
            elif self.name == '../Object/Shield/Shield_SoulShield.png':  # 소울실드 - 맵 당 한 번씩 빔 쏠 수 있음
                pass
            elif self.name == '../Object/Shield/Shield_ToyShield.png':  # 장난감 방패 - 반격 시 레고를 떨어트림 (지뢰같이 몬스터가 밟으면 데미지 입음)
                pass
        if self.judge_attack:
            self.judge_attack = False
