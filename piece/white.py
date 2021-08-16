from piece.piece import *


class White(Piece):
    img = ORANGEP
    isHuman = True

    def computeMoves(self, board):
        self.addMove(self.getLeftMove(board))
        self.addMove(self.getRightMove(board))
        self.addMove(self.getLeftKill(board))
        self.addMove(self.getRightKill(board))

