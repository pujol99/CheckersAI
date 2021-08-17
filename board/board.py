import json
from piece.black import Black
from piece.white import White
from piece.blackQueen import BlackQueen
from piece.whiteQueen import WhiteQueen
from piece.blank import Blank
from piece.piece import *
from board.turn import Turn
from board.action import *


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
        self.turn.pieceSelected.selectAsOrigin()
        for move in self.turn.pieceSelected.moves:
            move.lastStep().selectAsEnd()

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

    def getBlankPiece(self):
        return Blank


def readFromJson(boardType):
    with open(f"./board/boards/{boardType}.json") as json_file:
        data = json.load(json_file)
        return set([
                pieceType(piece)(int(row), col)
                for row, pieces in data.items()
                for col, piece in enumerate(pieces)
            ])


def pieceType(id):
    if id == 1:
        return Black
    if id == -1:
        return White
    if id == 2:
        return BlackQueen
    if id == -2:
        return WhiteQueen
    else:
        return Blank


def getClickIndex(xClick, yClick):
    col = (xClick - 50) // 50
    row = (yClick - 50) // 50
    return col, row
