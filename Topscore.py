class Topscore:
    def __init__(self):
        self.high_score = self.initialize_top_score()
        print(self.high_score)

    def initialize_top_score(self):
        file = open("./topscore.txt", "r")
        try:
            topscore = int(file.read())
        except ValueError:
            topscore = 0
        file.close()
        return topscore

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
            self.save_top_score()
        return self.high_score

    def save_top_score(self):
        file = open("./topscore.txt", "w")
        file.write(str(self.high_score))
        file.close()
        