

class Action:
    def __init__(self, board):
        self.title = ""
        self.board = board

        self.init()


class SelectPieceToMove(Action):
    title = "Selecting a piece"

    def init(self):
        self.board.selectAvailablePieces()
        self.board.turn.movesInCache = True

    def update(self, xC, yC):
        if xC and yC:
            selectedPiece = self.board.getPieceIfOrigin(xC, yC)
            if selectedPiece:
                self.board.turn.pieceSelected = selectedPiece
                self.finish()

    def finish(self):
        self.board.addAction(SelectMove)


class SelectMove(Action):
    title = "Selecting a move"

    def init(self):
        self.board.selectAvailableMoves()

    def update(self, xC, yC):
        if xC and yC:
            moveEndPiece = self.board.getPieceIfEnd(xC, yC)
            if moveEndPiece:
                self.board.getMove(moveEndPiece).execute()
                self.finish()
            else:
                self.board.turn.rollBack()

    def finish(self):
        self.board.unselectAll()
        self.board.endTurn()
