import json
from piece.piece import *
from board.turn import Turn
from board.action import *
from board.move import *


class Board:
    def __init__(self):
        self.pieces = readFromJson("original")

        self.initializeTurn()

    def initializeTurn(self):
        self.turn = Turn()
        self.addAction(SelectPieceToMove)

    def getPieceIfOrigin(self, xClick, yClick):
        col, row = getClickIndex(xClick, yClick)
        piece = self.getPiece(col, row)
        return piece if piece and piece.isSelected == SELECTED_ORIGN else None

    def getPieceIfEnd(self, xClick, yClick):
        col, row = getClickIndex(xClick, yClick)
        piece = self.getPiece(col, row)
        return piece if piece and piece.isSelected == SELECTED_END else None

    def selectAvailablePieces(self):
        self.unselectAll()
        humanPieces = [piece
                       for piece in self.pieces
                       if piece.isHuman and not piece.isBlank]

        for piece in humanPieces:
            if not self.turn.movesInCache:
                piece.computeMoves(self)
            piece.selectAsOrigin()

    def selectAvailableMoves(self):
        self.unselectAll()
        for move in self.turn.pieceSelected.moves:
            move.selectMove()

    def getDirection(self, piece, dir, positions=1):
        return self.getPiece(piece.col + dir * positions, piece.row + (-positions if piece.isHuman else positions))

    def getDirectionMove(self, piece, dir):
        nextPiece = self.getDirection(piece, dir)
        return Move([piece, nextPiece], 0, self) if nextPiece and nextPiece.isBlank else None

    def getDirectionKill(self, piece, dir):
        nextPiece = self.getDirection(piece, dir)
        if nextPiece and not nextPiece.isBlank and nextPiece.isHuman != piece.isHuman:
            nextNextPiece = self.getDirection(piece, dir, 2)
            if nextNextPiece and nextNextPiece.isBlank:
                return Move([piece, nextPiece, nextNextPiece], 1, self)
        return None

    def unselectAll(self):
        for piece in self.pieces:
            piece.unselect()

    def clearAllMoves(self):
        for piece in self.pieces:
            piece.moves.clear()

    def getPiece(self, col, row):
        for piece in self.pieces:
            if piece.row == row and piece.col == col:
                return piece
        return None

    def addAction(self, action):
        self.turn.actions.append(action(self))

    def getMove(self, moveEnd):
        for move in self.turn.pieceSelected.moves:
            if move.lastStep() == moveEnd:
                return move
        return None

    def endTurn(self):
        self.turn = None


def readFromJson(boardType):
    with open(f"./board/boards/{boardType}.json") as json_file:
        data = json.load(json_file)
        return set([
                Piece(int(row), col, piece)
                for row, pieces in data.items()
                for col, piece in enumerate(pieces)
            ])


def getClickIndex(xClick, yClick):
    col = (xClick - 50) // 50
    row = (yClick - 50) // 50
    return col, row
