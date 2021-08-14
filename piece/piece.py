from constants import *


class Piece:
	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.screenX = 50 + x*50
		self.screenY = 50 + y*50
	
	def draw(self, screen):
		if self.img:
			screen.blit(self.img, (self.screenX, self.screenY))
