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

while True:  #main script
    user_input = input('To take a swing hit h, to take a pitch hit p or q for quit s for scoreboard\n')
    if user_input == 'q':#for q on keyboard
        print("Game over")
        break
    if user_input == 'h' or user_input == 'H': #for h on the keyboard
        strikes_hits_score(1)
    elif user_input == 'p' or user_input == "P":#for p on the keyboard
        balls(1)
    elif user_input == 's' or user_input == 'S': #for s on the keyboard
        runs = sum(ScoreBoard.run_count)#adds up the runs
        strikes = sum(ScoreBoard.strike_count)#adds up the strikes
        ball = sum(ScoreBoard.ball_count)#adds up the balls
        hits = sum(ScoreBoard.hit_count)#adds up the hits
        print(f'ScoreBoard\nRuns: {runs}\nHits: {hits}\nStriks: {strikes}\nBalls: {ball}')
    else:
        print('Try again')
