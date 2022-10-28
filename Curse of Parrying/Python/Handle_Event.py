from pico2d import *

running = True


def handle_events(Player, Interact_MonsterBox, Interact_MonsterBox2, Interact_BlueShield, Interact_RedCrossShield, Monster, Shields,
                  Player_Parrying, Monsters, enemy_variable):
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
                Player_Parrying.do = True
            # 상호작용
            elif event.key == SDLK_f:
                # 몬스터박스
                if Interact_MonsterBox.judge:
                    if not Monster.summon:
                        Monster.summon = True
                    elif Monster.summon:
                        Monster.summon = False
                        Monster.frame = 0
                # 몬스터박스2
                if Interact_MonsterBox2.judge:
                    if enemy_variable.monster_summon == False:
                        enemy_variable.monster_judge = True
                    elif enemy_variable.monster_summon == True:
                        enemy_variable.monster_summon = False
                        for i in Monsters:
                            i.frame = 0
                # 파랑방패
                if Interact_BlueShield.judge == True:
                    if Shields[0].judge_click == False:
                        Shields[0].judge_click = True
                        Player.damage = 15
                    elif Shields[0].judge_click == True:
                        Shields[0].judge_click = False
                        Player.damage = 10
                        Player_Parrying.shieldNone = True
                # 적십자방패
                if Interact_RedCrossShield.judge == True:
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
