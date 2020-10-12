# baseball game
# function for strikes and balls and keep track
# function outs and something to keep track of outs
# function for hit and keep track of hits
# function for runs and keep track of runs
# way to keep score
# if I take a swing I can either get a hit or strike

import random

from Ball import balls
from Strike import strikes_hits_score
from ScoreBoard import ScoreBoard
import Strike

print("Baseball game")











while True:  # figure out how to stop program after 3 outs
    user_input = input('To take a swing hit h, to take a pitch hit p or q for quit s for scoreboard\n')
    if user_input == 'q':
        print("Game over")
        break
    if user_input == 'h' or user_input == 'H':
        strikes_hits_score(1)
    elif user_input == 'p' or user_input == "P":

        balls(1)
    elif user_input == 's' or user_input == 'S':
        runs = sum(ScoreBoard.run_count)
        strikes = sum(ScoreBoard.strike_count)
        ball = sum(ScoreBoard.ball_count)
        hits = sum(ScoreBoard.hit_count)
        print(f'ScoreBoard\nRuns: {runs}\nHits: {hits}\nStriks: {strikes}\nBalls: {ball}')
    else:
        print('Try again')
