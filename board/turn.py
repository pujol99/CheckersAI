

class Turn:
    def __init__(self):
        self.actions = []

        self.pieceSelected = None
        self.movesInCache = False

    def doAction(self, xC, yC):
        self.actions[-1].update(xC, yC)

    def initializeAction(self):
        self.actions[-1].init()

    def rollBack(self):
        self.actions.pop()
        self.initializeAction()

