import random
from ScoreBoard import ScoreBoard
from Outs import outs
def balls(ball):
    ball_result = ball
    if ball == 1:
        if random.random() <= .45:
            ScoreBoard.ball_count.append(ball_result)
            ball_number = sum(ScoreBoard.ball_count)
            print(f'Its a ball:{ball_number}')
            if ball_number == 4:
                ScoreBoard.ball_count.clear()
                ScoreBoard.hit_count.append(ball_result)
                ScoreBoard.ball_count.clear()
                ScoreBoard.strike_count.clear()
                return print("take your base")
        else:
            ScoreBoard.strike_count.append(ball_result)
            striked = sum(ScoreBoard.strike_count)
            print(f"Strike:{striked}")
            if striked == 3:
                ScoreBoard.ball_count.clear()
                ScoreBoard.strike_count.clear()
                outs(ball_result)
