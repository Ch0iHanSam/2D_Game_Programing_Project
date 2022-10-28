from pico2d import *

running = True


def handle_events(Player, Interact_MonsterBox, Interact_BlueShield, Interact_RedCrossShield, Monster, Shields,
                  Player_Parrying):
    global running
    events = get_events()
    for event in events:
        # 종료
        if event.type == SDL_QUIT:
            running = False
            pass
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            pass
        # 키다운
        elif event.type == SDL_KEYDOWN:
            # 캐릭터 이동
            if event.key == SDLK_RIGHT:
                Player.dir_x += 1
            elif event.key == SDLK_LEFT:
                Player.dir_x -= 1
            elif event.key == SDLK_UP:
                Player.dir_y += 1
            elif event.key == SDLK_DOWN:
                Player.dir_y -= 1
            # 패링
            elif event.key == SDLK_x:
                Player.parrying = True
                Player_Parrying.do = True
            # 상호작용
            elif event.key == SDLK_f:
                if Interact_MonsterBox.judge == 'on':
                    if Monster.summon == 'off':
                        Monster.summon = 'on'
                    elif Monster.summon == 'on':
                        Monster.summon = 'off'
                        Monster.frame = 0
                if Interact_BlueShield.judge == 'on':
                    if Shields[0].judge_click == False:
                        Shields[0].judge_click = True
                        Player.damage = 15
                    elif Shields[0].judge_click == True:
                        Shields[0].judge_click = False
                        Player.damage = 10
                        Player_Parrying.shieldNone = True
                if Interact_RedCrossShield.judge == 'on':
                    if Shields[1].judge_click == False:
                        Shields[1].judge_click = True
                    elif Shields[1].judge_click == True:
                        Shields[1].judge_click = False
                        Player_Parrying.shieldNone = True
        # 키업
        elif event.type == SDL_KEYUP:
            # 캐릭터 정지
            if event.key == SDLK_RIGHT:
                Player.dir_x -= 1
            elif event.key == SDLK_LEFT:
                Player.dir_x += 1
            elif event.key == SDLK_UP:
                Player.dir_y -= 1
            elif event.key == SDLK_DOWN:
                Player.dir_y += 1
