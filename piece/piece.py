from constants import *
from board.move import *


class Piece:

	isSelected = None
	isBlank = False
	isHuman = False

	def __init__(self, row, col):
		self.col = col
		self.row = row
		self.screenX = 50 + col*50
		self.screenY = 50 + row*50
		self.moves = []

	def clearMoves(self):
		self.moves.clear()

	def draw(self, screen):
		if self.isSelected:
			screen.blit(self.isSelected, (self.screenX, self.screenY))
		if self.img:
			screen.blit(self.img, (self.screenX, self.screenY))

	def getRight(self, board, positions=1):
		return board.getPiece(self.col + positions, self.row + (-positions if self.isHuman else positions))

	def getRightMove(self, board):
		piece = self.getRight(board)
		return Move([self, piece], 0, board) if piece and piece.isBlank else None

	def getRightKill(self, board):
		piece = self.getRight(board)
		if piece and not piece.isBlank and piece.isHuman != self.isHuman:
			nextPiece = self.getRight(board, 2)
			if nextPiece and nextPiece.isBlank:
				return Move([self, piece, nextPiece], 1, board)
		return None

	def getLeft(self, board, positions=1):
		return board.getPiece(self.col - positions, self.row + (-positions if self.isHuman else positions))

	def getLeftMove(self, board):
		piece = self.getLeft(board)
		return Move([self, piece], 0, board) if piece and piece.isBlank else None

	def getLeftKill(self, board):
		piece = self.getLeft(board)
		if piece and not piece.isBlank and piece.isHuman != self.isHuman:
			nextPiece = self.getLeft(board, 2)
			if nextPiece and nextPiece.isBlank:
				return Move([self, piece, nextPiece], 1, board)
		return None

	def selectAsEnd(self):
		self.isSelected = SELECTED_END

	def selectedKill(self):
		self.isSelected = SELECTED_KILL

	def selectAsOrigin(self):
		if len(self.moves) > 0:
			self.isSelected = SELECTED_ORIGN

	def unselect(self):
		self.isSelected = None

	def addMove(self, move):
		if move:
			self.moves.append(move)

	def setPos(self, row, col):
		self.col = col
		self.row = row
		self.screenX = 50 + self.col * 50
		self.screenY = 50 + self.row * 50
