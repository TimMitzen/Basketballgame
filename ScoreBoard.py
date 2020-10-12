class ScoreBoard:#keeps track of the outs, hit, balls , inning and runs

    strike_count =[]
    hit_count = []
    ball_count = []
    out_count = []
    run_count = []
    inning_count = []

    def __init__(self, strike_count, hit_count, ball_count, out_count, run_count, inning_count):
        self.strike_count = strike_count
        self.ball_count = ball_count
        self.out_count = out_count
        self.hit_count = hit_count
        self.run_count = run_count
        self.inning_count = inning_count
