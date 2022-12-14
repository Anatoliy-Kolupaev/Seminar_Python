import Game1
import Game2
import View
import Logger

def run():
    mode = View.choose_mood()
    if mode == '1':
        result = Game1.run_game()
        Logger.log_result(result)
    if mode == '2':
        result = Game2.run_game()
        Logger.log_result(result)


