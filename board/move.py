

class Move:
    def __init__(self, steps, kills, board):
        self.steps = steps
        self.kills = kills
        self.board = board

    def execute(self):
        self.board.unselectAll()
        # swap first and last step
        self.board.pieces.add(
            self.board.getBlankPiece()(self.steps[0].row, self.steps[0].col))
        self.steps[0].setPos(self.steps[-1].row, self.steps[-1].col)
        self.board.pieces.remove(self.steps[-1])

        # intermidiate steps go blank
        for step in self.steps[:-2]:
            self.board.pieces.remove(step)
            self.board.pieces.add(
                self.board.getBlankPiece()(step.row, step.col)
            )

    def lastStep(self):
        return self.steps[-1]
