from piece.piece import Piece


class Move:
    def __init__(self, steps, kills, board):
        self.steps = steps
        self.kills = kills
        self.board = board

    def execute(self):
        # swap first and last step
        firstStep = self.firstStep()
        self.board.pieces.add(
            Piece(firstStep.row, firstStep.col, 'n'))

        lastStep = self.lastStep()
        firstStep.setPos(lastStep.row, lastStep.col)
        self.board.pieces.remove(lastStep)

        # intermediate steps go blank
        for step in self.intermediateSteps():
            self.board.pieces.remove(step)
            self.board.pieces.add(
                Piece(step.row, step.col, 'n'))

    def selectMove(self):
        self.selectStart()
        self.selectKills()
        self.selectEnd()

    def selectKills(self):
        for step in self.intermediateSteps():
            if not step.isBlank:
                step.selectedKill()

    def selectStart(self):
        self.firstStep().selectAsOrigin()

    def selectEnd(self):
        self.lastStep().selectAsEnd()

    def firstStep(self):
        return self.steps[0]

    def lastStep(self):
        return self.steps[-1]

    def intermediateSteps(self):
        return self.steps[1:-1]
