import random
from ScoreBoard import ScoreBoard
from Outs import outs
def balls(ball):
    ball_result = ball
    if ball == 1: #for p button
        if random.random() <= .45: #makes it random to 45 percent
            ScoreBoard.ball_count.append(ball_result)#adds to to ball_count
            ball_number = sum(ScoreBoard.ball_count)#adds to ball_count
            print(f'Its a ball:{ball_number}')
            if ball_number == 4:
                ScoreBoard.ball_count.clear()#clears
                ScoreBoard.hit_count.append(ball_result)#adds ball_count
                ScoreBoard.ball_count.clear()#clears
                ScoreBoard.strike_count.clear()#clears
                return print("take your base")
        else:
            ScoreBoard.strike_count.append(ball_result)#adds to strike_count
            striked = sum(ScoreBoard.strike_count)#adds strike_count
            print(f"Strike:{striked}")
            if striked == 3:
                ScoreBoard.ball_count.clear()#clears
                ScoreBoard.strike_count.clear()#clears
                outs(ball_result)#runs outs function
