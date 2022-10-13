from pico2d import *


# 테스트용 몬스터 클래스
class Test_Monster:
    def __init__(self):
        self.image = load_image('../Object/Enemy/Stage1/Pigeon/Enemy_Pigeon_Attack.png')
        self.x, self.y = 100, 200
        self.frame = 0
        self.summon = 'off'

    def draw(self):
        if self.summon == 'on':
            self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.summon == 'on':
            self.frame = (self.frame+1)%9


# 테스트용 몬스터의 공격 이펙트 클래스
class Test_Monster_Attack_Effect:
    def __init__(self):
        self.image = load_image('../Effect/Monster/Monster_Attack/Pigeon/Pigeon_Attack.png')
        self.x, self.y = 100, 200
        self.frame = 0
        self.judge = 'off'

    def draw(self):
        if self.judge == 'on':
            if self.x < 700:
                self.image.clip_draw(self.frame*68, 0, 68, 68, self.x, self.y)

    def update(self):
        if self.judge == 'on':
            self.frame = (self.frame+1)%7
            self.x += 10
        if self.x > 700:
            self.judge = 'off'


# 상호작용 클래스
class Interact:
    def __init__(self):
        self.image = load_image('../Effect/ETC/interact.png')
        self.x, self.y = 0, 0
        self.judge = 'off'

    def draw(self, Object):
        bndry = 50
        if (Object.x + bndry > self.x > Object.x - bndry) and (Object.y + bndry > self.y > Object.y - bndry):
            self.judge = 'on'
            self.image.draw(self.x, self.y)
        else:
            self.judge = 'off'

    def set_xy(self, Player):
        self.x, self.y = Player.x, Player.y


# 몬스터 박스 클래스
class MonsterBox:
    def __init__(self):
        self.image = load_image('../Object/ETC/MonsterBox.png')
        self.x, self.y = 700, 500

    def draw(self):
        self.image.draw(self.x, self.y)


# 배경 클래스
class Background:
    def __init__(self):
        self.image = load_image('../BackGround/Practice.png')
        self.x, self.y = 400, 300

    def draw(self):
        self.image.draw(self.x, self.y)


# 플레이어 걷기 클래스
class Player:
    def __init__(self):
        self.image = load_image('../Object/Character/Walking/Character_Player_Walking.png')
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 'idle'
        self.exdir = 'right'
        self.dash = 'off'
        self.parrying = 'off'

    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'up':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'down':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.image.clip_draw(2 * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(2 * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
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


# 대쉬 클래스
class Player_Dash:
    def __init__(self):
        self.image = load_image('../Object/Character/Dash/Character_Player_Dash.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir = ' '
        self.exdir = ' '

    def draw(self):
        if self.dir == 'right':
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.dir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'up':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'down':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
            elif self.exdir == 'left':
                self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def set_dir(self, Player):
        self.dir = Player.dir
        self.exdir = Player.exdir
        self.x = Player.x
        self.y = Player.y

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.dir == 'right':
            self.x += 10
            Player.x = self.x
        elif self.dir == 'left':
            self.x -= 10
            Player.x = self.x
        elif self.dir == 'up':
            self.y += 10
            Player.y = self.y
        elif self.dir == 'down':
            self.y -= 10
            Player.y = self.y
        elif self.dir == 'idle':
            if self.exdir == 'right':
                self.x += 10
                Player.x = self.x
            elif self.exdir == 'left':
                self.x -= 10
                Player.x = self.x


# 패링 클래스
class Player_Parrying:
    def __init__(self):
        self.image = load_image('../Object/Character/Parrying/Character_Player_Parrying.png')
        self.x, self.y = 0, 0
        self.frame = 0
        self.exdir = ' '

    def draw(self):
        if self.exdir == 'right':
            self.image.clip_draw(self.frame * 68, 68, 68, 68, self.x, self.y)
        elif self.exdir == 'left':
            self.image.clip_draw(self.frame * 68, 0, 68, 68, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 9

    def set_exdir(self, Player):
        self.exdir = Player.exdir
        self.x, self.y = Player.x, Player.y


# 이벤트 받기 함수
def handle_events(Player, Monster, Interact):
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_f:
            if Interact.judge == 'on':
                if Monster.summon == 'off':
                    Monster.summon = 'on'
                elif Monster.summon == 'on':
                    Monster.summon = 'off'
                    Monster.frame = 0


# 기본 세팅
open_canvas()
running = True
Player = Player()
Background = Background()
Player_Dash = Player_Dash()
Player_Parrying = Player_Parrying()
MonsterBox = MonsterBox()
Interact = Interact()
Test_Monster = Test_Monster()
Effect = [Test_Monster_Attack_Effect() for i in range(1)]
num = 0
num2 = 1

# 게임 내부
while running:
    # 멈춤상태
    clear_canvas()
    Background.draw()
    # 캐릭터 그리기
    Player.draw()
    # 상호작용 그리기
    Interact.set_xy(Player)
    Interact.draw(MonsterBox)
    # 몬스터 박스 그리기
    MonsterBox.draw()
    # 테스트 몬스터 그리기
    Test_Monster.draw()
    Test_Monster.update()
    # 테스트 몬스터의 공격 이펙트 그리기
    if Test_Monster.summon == 'on':
        num2 = (num2+1)%2
        for effect in Effect:
            effect.draw()
            effect.update()
            if len(Effect) == 10:
                Effect.pop(0)
        if num2 == 0:
            if Test_Monster.frame == 3:
                Effect.append(Test_Monster_Attack_Effect())
                Effect[num].judge = 'on'
                if num < 9:
                    num += 1
    # 캔버스 업데이트
    update_canvas()
    # 입력 받기
    handle_events(Player, Test_Monster, Interact)
    # 대쉬
    if Player.dash == 'on':
        Player_Dash.set_dir(Player)
        for a in range(8):
            clear_canvas()
            Background.draw()
            Player_Dash.draw()
            MonsterBox.draw()
            Test_Monster.draw()
            Test_Monster.update()
            if Test_Monster.summon == 'on':
                num2 = (num2 + 1) % 2
                for effect in Effect:
                    effect.draw()
                    effect.update()
                    if len(Effect) == 10:
                        Effect.pop(0)
                if num2 == 0:
                    if Test_Monster.frame == 3:
                        Effect.append(Test_Monster_Attack_Effect())
                        Effect[num].judge = 'on'
                        if num < 9:
                            num += 1
            update_canvas()
            Player_Dash.update()
            delay(0.01)
        Player.dash = 'off'
    # 패링
    if Player.parrying == 'on':
        Player_Parrying.set_exdir(Player)
        for a in range(9):
            clear_canvas()
            Background.draw()
            Player_Parrying.draw()
            MonsterBox.draw()
            Test_Monster.draw()
            Test_Monster.update()
            if Test_Monster.summon == 'on':
                num2 = (num2 + 1) % 2
                for effect in Effect:
                    effect.draw()
                    effect.update()
                    if len(Effect) == 10:
                        Effect.pop(0)
                if num2 == 0:
                    if Test_Monster.frame == 3:
                        Effect.append(Test_Monster_Attack_Effect())
                        Effect[num].judge = 'on'
                        if num < 9:
                            num += 1
            update_canvas()
            Player_Parrying.update()
            delay(0.05)
        Player.parrying = 'off'
    # 움직임 상태
    while Player.dir != 'idle':
        clear_canvas()
        Background.draw()
        Player.draw()
        Interact.set_xy(Player)
        Interact.draw(MonsterBox)
        MonsterBox.draw()
        Test_Monster.draw()
        Test_Monster.update()
        if Test_Monster.summon == 'on':
            num2 = (num2 + 1) % 2
            for effect in Effect:
                effect.draw()
                effect.update()
                if len(Effect) == 10:
                    Effect.pop(0)
            if num2 == 0:
                if Test_Monster.frame == 3:
                    Effect.append(Test_Monster_Attack_Effect())
                    Effect[num].judge = 'on'
                    if num < 9:
                        num += 1
        update_canvas()
        Player.set_exdir()
        handle_events(Player, Test_Monster, Interact)
        # 대쉬
        if Player.dash == 'on':
            Player_Dash.set_dir(Player)
            for a in range(8):
                clear_canvas()
                Background.draw()
                Player_Dash.draw()
                MonsterBox.draw()
                Test_Monster.draw()
                Test_Monster.update()
                if Test_Monster.summon == 'on':
                    num2 = (num2 + 1) % 2
                    for effect in Effect:
                        effect.draw()
                        effect.update()
                        if len(Effect) == 10:
                            Effect.pop(0)
                    if num2 == 0:
                        if Test_Monster.frame == 3:
                            Effect.append(Test_Monster_Attack_Effect())
                            Effect[num].judge = 'on'
                            if num < 9:
                                num += 1
                update_canvas()
                Player_Dash.update()
                delay(0.01)
            Player.dash = 'off'
        # 패링
        if Player.parrying == 'on':
            Player_Parrying.set_exdir(Player)
            for a in range(9):
                clear_canvas()
                Background.draw()
                Player_Parrying.draw()
                MonsterBox.draw()
                Test_Monster.draw()
                Test_Monster.update()
                if Test_Monster.summon == 'on':
                    num2 = (num2 + 1) % 2
                    for effect in Effect:
                        effect.draw()
                        effect.update()
                        if len(Effect) == 10:
                            Effect.pop(0)
                    if num2 == 0:
                        if Test_Monster.frame == 3:
                            Effect.append(Test_Monster_Attack_Effect())
                            Effect[num].judge = 'on'
                            if num < 9:
                                num += 1
                update_canvas()
                Player_Parrying.update()
                delay(0.05)
            Player.parrying = 'off'
        Player.update()
        delay(0.05)
    delay(0.05)

# 마무리
del Player
del Background
del Player_Dash

close_canvas()
