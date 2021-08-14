
class Piece:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.moves = []
		self.queen = False
		
		self.toplk = True
		self.toprk = True
		self.downlk = True
		self.downrk = True
	
	def select_piece(self, screen, img, pos):
		screen.blit(img, pos)
	
	def draw_piece(self, img, pos, screen):
		screen.blit(img, pos)
			
	def reset_moves(self):
		self.moves.clear()
