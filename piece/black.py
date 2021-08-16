from piece.piece import *


class Black(Piece):
    img = BROWNP

    def computeMoves(self, board):
        self.addMove(self.getLeftMove(board))
        self.addMove(self.getRightMove(board))
        self.addMove(self.getLeftKill(board))
        self.addMove(self.getRightKill(board))