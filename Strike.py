from ScoreBoard import ScoreBoard
import random
from Outs import outs


def strikes_hits_score(strike):
    strikes_count = strike

    if strike == 1:
        if random.random() <= .65:#random 65 percent
            ScoreBoard.strike_count.append(strikes_count)#adds to strike_count
            striked = sum(ScoreBoard.strike_count)#adds up the strike count
            print(f"Strike:{striked}")
            if striked == 3:

                ScoreBoard.strike_count.clear()#clears
                ScoreBoard.ball_count.clear()#clears
                outs(strikes_count)#runs the out function



        else:
            ScoreBoard.hit_count.append(strikes_count)#adds to hit_count
            ScoreBoard.ball_count.clear()#clears
            ScoreBoard.strike_count.clear()#clears
            hitted = sum(ScoreBoard.hit_count)#clears

            print(f"You got an hit! Men on base: {hitted}")
            if hitted == 4:
                ScoreBoard.hit_count.clear()#clears
                ScoreBoard.run_count.append(strikes_count)#adds to strike count
                ScoreBoard.ball_count.clear()#clears
                ScoreBoard.strike_count.clear()#clears

                runs = sum(ScoreBoard.run_count)#adds all the runs
                print(f'Scored, Your score {runs}')
                if runs == 5:
                    quit(f"You won\nScore:{runs}")
