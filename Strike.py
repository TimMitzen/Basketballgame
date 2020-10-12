from ScoreBoard import ScoreBoard
import random
from Outs import outs
from Outs import inning

def strikes_hits_score(strike):
    strikes_count = strike

    if strike == 1:
        if random.random() <= .65:
            ScoreBoard.strike_count.append(strikes_count)
            striked = sum(ScoreBoard.strike_count)
            print(f"Strike:{striked}")
            if striked == 3:

                ScoreBoard.strike_count.clear()
                ScoreBoard.ball_count.clear()
                outs(strikes_count)



        else:
            ScoreBoard.hit_count.append(strikes_count)
            ScoreBoard.ball_count.clear()
            ScoreBoard.strike_count.clear()
            hitted = sum(ScoreBoard.hit_count)

            print(f"You got an hit! Men on base: {hitted}")
            if hitted == 4:
                ScoreBoard.hit_count.clear()
                ScoreBoard.run_count.append(strikes_count)
                ScoreBoard.ball_count.clear()
                ScoreBoard.strike_count.clear()

                runs = sum(ScoreBoard.run_count)
                print(f'Scored, Your score {runs}')
                if runs == 5:
                    quit(f"You won\nScore:{runs}")
