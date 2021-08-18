from piece.pieceUtils import *


class Piece:
	def __init__(self, row, col, identification):
		self.setPos(row, col)
		self.moves = []
		self.setId(identification)
		self.isSelected = None

	def draw(self, screen):
		if self.isSelected:
			screen.blit(self.isSelected, (self.screenX, self.screenY))
		if self.img:
			screen.blit(self.img, (self.screenX, self.screenY))

	def computeMoves(self, board):
		for moveType in [board.getDirectionMove, board.getDirectionKill]:
			for direction in [LEFT, RIGHT]:
				self.addMove(moveType(self, direction))

	def addMove(self, move):
		if move:
			self.moves.append(move)

	def selectAsEnd(self):
		self.isSelected = SELECTED_END

	def selectedKill(self):
		self.isSelected = SELECTED_KILL

	def selectAsOrigin(self):
		if len(self.moves) > 0:
			self.isSelected = SELECTED_ORIGN

	def unselect(self):
		self.isSelected = None

	def setPos(self, row, col):
		self.col, self.row = col, row
		self.screenX = 50 + self.col * 50
		self.screenY = 50 + self.row * 50

	def setId(self, identification):
		self.identification = identification
		self.setStatus()

	def setStatus(self):
		self.isBlank = getPieceIsBlank(self.identification)
		self.isHuman = getPieceIsHuman(self.identification)
		self.img = getPieceImage(self.identification)

	def clearMoves(self):
		self.moves.clear()
