import json
from piece.black import Black
from piece.white import White
from piece.blackQueen import BlackQueen
from piece.whiteQueen import WhiteQueen
from piece.blank import Blank
from piece.piece import *
from board.turn import Turn
from stages.action import *


class Board:
    def __init__(self):
        self.pieces = []
        self.readFromJson("original")

        self.turn = Turn()
        self.addAction(SelectPieceToMove)

    def readFromJson(self, boardType):
        with open(f"./board/boards/{boardType}.json") as json_file:
            data = json.load(json_file)

        for row, pieces in data.items():
            self.pieces.append([
                pieceType(piece)(int(row), col) for col, piece in enumerate(pieces)
            ])

    def getPieceIfOrigin(self, xClick, yClick):
        col, row = getClickIndex(xClick, yClick)
        piece = self.getPiece(col, row)
        return piece if piece and piece.isSelected == SELECTED_ORIGN else None

    def getPieceIfEnd(self, xClick, yClick):
        col, row = getClickIndex(xClick, yClick)
        piece = self.getPiece(col, row)
        return piece if piece and piece.isSelected == SELECTED_END else None

    def selectAvailablePieces(self):
        """
        Select pieces that can be moved and get more kills
        """
        self.unselectAll()
        humanPieces = [piece
                       for row in self.pieces
                       for piece in row
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
        for row in self.pieces:
            for piece in row:
                piece.unselect()

    def makeCopy(self):
        return [row[:] for row in self.pieces]

    def getPiece(self, col, row):
        return self.pieces[row][col] if validPos(row, col) else None

    def addAction(self, action):
        self.turn.actions.append(action(self))

    def getPieceMove(self, moveEnd):
        for move in self.turn.pieceSelected.moves:
            if move.lastStep() == moveEnd:
                return move
        return None

    def finishTurn(self):
        self.turn = None


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


def validPos(row, col):
    return 0 <= row <= 7 and 0 <= col <= 7


def getClickIndex(xClick, yClick):
    col = (xClick - 50) // 50
    row = (yClick - 50) // 50
    return col, row
