import start_state
import game_framework
import pico2d


# play_state.Run()

pico2d.open_canvas()
game_framework.run(start_state)
pico2d.close_canvas()