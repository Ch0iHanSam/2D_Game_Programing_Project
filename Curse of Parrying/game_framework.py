import time
frame_time = 0.0

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)


running = None
stack = []
ex_state = None

def get_prev_state():
    try:
        return stack[-2]  # 이전 state 반환
    except:
        return None  # 없으면 None(아마 버그방지인듯)


def change_state(state):
    global stack, ex_state
    if(len(stack)>0):
        stack[-1].exit()  # 현재 state의 exit함수 실행
        ex_state = stack[-1]
        stack.pop()  # 현재 state 삭제 (state 변경이니까 현재와 관계 없음)
    stack.append(state)
    state.enter()


def push_state(state):
    global stack
    if (len(stack)>0):
        stack[-1].pause()  # 현재 state 일시정지 (현재 state위에 새로운 state를 밀어넣는 거임)
    stack.append(state)
    state.enter()


def pop_state():
    global stack
    if (len(stack)>0):
        stack[-1].exit()  # 그냥 현재 state나가기
        stack.pop()

    if (len(stack)>0):
        stack[-1].resume()  # 앞에서 나갔으니까 밑에 깔려있던 pause상태인 state를 재시작함


def quit():
    global running
    running = False


def fill_states(*states):
    for state in states:
        stack.append(state)


def run(start_state):
    global running, stack
    running = True

    for state in stack:  # stack에 담겨져있는 모든 state 실행 (미리 실행해야하는 state가 있다면)
        state.enter()
        state.pause()  # 그리고 일시정지 상태

    stack.append(start_state)  # start_state로 지정해놓은 state 추가하기
    stack[-1].enter()  # start_state로 들어가기

    current_time = time.time()
    while running:
        stack[-1].handle_events()  # 현재 state의 진행
        stack[-1].update()
        stack[-1].draw()  # state 삭제할 때까지 반복
        global frame_time
        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time
        # print(f'Frame Time: {frame_time}, Frame Rate: {frame_rate}')

    while (len(stack) > 0):
        stack[-1].exit() # 게임 진행이 끝났는데 state가 남아있다면 전부다 나가고 삭제하기
        stack.pop()


def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)

if __name__ == '__main__':
    test_game_framework()