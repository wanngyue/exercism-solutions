class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def highest(self):
        return max(self.scores)

    def top(self):
        return sorted(self.scores)[::-1][:3]

    def report(self):
        recent = self.latest()
        highest = self.highest()
        if recent == highest:
            return "Your latest score was %d. That's your personal best!" % recent
        else:
            return "Your latest score was %d. That's %d short of your personal best!" % (recent, highest - recent)
