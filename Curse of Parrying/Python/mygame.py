import play_state
import game_framework
import pico2d


# play_state.Run()

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.close_canvas()