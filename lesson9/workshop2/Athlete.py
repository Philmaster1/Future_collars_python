class Athlete:
    def __init__(self, sport, team):
        self.sport = sport
        self.team = team

    def train(self):
        print(f"Training in {self.sport} for team {self.team}")
