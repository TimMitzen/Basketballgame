from ScoreBoard import ScoreBoard
def outs(out):
    outs_counts = out

    ScoreBoard.out_count.append(outs_counts)
    ScoreBoard.hit_count.clear()
    ScoreBoard.ball_count.clear()
    ScoreBoard.strike_count.clear()
    num_outs = sum(ScoreBoard.out_count)
    print(f'You are out! Outs: {num_outs}')
    if num_outs == 3:

        inning(outs_counts)

def inning(innings):

    innings_count = innings
    ScoreBoard.inning_count.append(innings_count)
    ScoreBoard.out_count.clear()
    ScoreBoard.hit_count.clear()
    ScoreBoard.strike_count.clear()
    ScoreBoard.ball_count.clear()
    num_innings = sum(ScoreBoard.inning_count)
    score = sum(ScoreBoard.run_count)
    print(f'Inning over! Inning: {num_innings}')
    if num_innings == 2:
        quit(f"Game over,Score:{score}")







