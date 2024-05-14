#Source: https://stackoverflow.com/questions/56847143/typeerror-not-supported-between-instances-of-builtin-function-or-method-a
class Yatzy:
    def __init__(self, humans_num, bots_num):(...)

    @property
    def players_scores(self):
        scores = {}
        for i in range(len(self.humans)):
            scores[self.humans[i].name] = self.humans[i].total_score
        for i in range(len(self.bots)):
            scores[self.bots[i].name] = self.bots[i].total_score
        print(type(self.bots[0].name), type(self.bots[0].total_score))
        return scores

    def game_loop(self):
        print('Welcome to Yatzy game!')
        round_counter = 1
        while round_counter <= self.MAX_ROUNDS:(...)
        print("Final score:", self.players_scores)
        print(type(self.players_scores), type(self.players_scores.keys()), type(self.players_scores.values()))
        best_player = max(self.players_scores, self.players_scores.get)
        print("{} won with {}".format(best_player, self.players_scores[best_player]))

game = Yatzy(humans_num=0, bots_num=4)
game.game_loop()