from ScoreBoard import ScoreBoard
def outs(out):
    outs_counts = out

    ScoreBoard.out_count.append(outs_counts)#adds
    ScoreBoard.hit_count.clear()#clears
    ScoreBoard.ball_count.clear()#clears
    ScoreBoard.strike_count.clear()#clears
    num_outs = sum(ScoreBoard.out_count)#adds up out count
    print(f'You are out! Outs: {num_outs}')
    if num_outs == 3:

        inning(outs_counts)#runs inning function

def inning(innings):

    innings_count = innings
    ScoreBoard.inning_count.append(innings_count)#adds to inning count
    ScoreBoard.out_count.clear()#clears
    ScoreBoard.hit_count.clear()#clears
    ScoreBoard.strike_count.clear()#clears
    ScoreBoard.ball_count.clear()#clears
    num_innings = sum(ScoreBoard.inning_count)#adds the innings
    score = sum(ScoreBoard.run_count)#adds the innings
    print(f'Inning over! Inning: {num_innings}')
    if num_innings == 2:
        quit(f"Game over,Score:{score}")







