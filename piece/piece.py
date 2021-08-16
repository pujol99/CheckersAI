from constants import *
from board.move import *


class Piece:

	isSelected = None
	isBlank = False
	isHuman = False

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.screenX = 50 + x*50
		self.screenY = 50 + y*50
		self.moves = []

	def clearMoves(self):
		self.moves.clear()

	def draw(self, screen):
		if self.isSelected:
			screen.blit(self.isSelected, (self.screenX, self.screenY))
		if self.img:
			screen.blit(self.img, (self.screenX, self.screenY))

	def getRight(self, board):
		return board.getPiece(self.x + 1, self.y + (-1 if self.isHuman else 1))

	def getRightMove(self, board):
		piece = self.getRight(board)
		return Move([self, piece], 0, board) if piece and piece.isBlank else None

	def getRightKill(self, board):
		piece = self.getRight(board)
		if piece and piece.isHuman != self.isHuman:
			nextPiece = piece.getRight(board)
			if nextPiece and nextPiece.isBlank:
				return Move([self, piece, nextPiece], 1, board)
		return None

	def getLeft(self, board):
		return board.getPiece(self.x - 1, self.y + (-1 if self.isHuman else 1))

	def getLeftMove(self, board):
		piece = self.getLeft(board)
		return Move([self, piece], 0, board) if piece and piece.isBlank else None

	def getLeftKill(self, board):
		piece = self.getLeft(board)
		if piece and piece.isHuman != self.isHuman:
			nextPiece = piece.getLeft(board)
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
