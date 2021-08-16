
class Move:
    def __init__(self, steps, kills, board):
        self.steps = steps
        self.kills = kills
        self.board = board

    def execute(self):
        self.board.unselectAll()

    def lastStep(self):
        return self.steps[-1]
