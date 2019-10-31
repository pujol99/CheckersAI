import pygame
import time

class Piece:
	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.value = value
		self.moves = []
		self.queen = False
		
		self.topl = True
		self.topr = True
		self.downl = True
		self.downr = True
		
		self.toplk = True
		self.toprk = True
		self.downlk = True
		self.downrk = True
	
	def posible_moves(self, bo, rec=False, x=None, y=None, kills=0):
		value = self.value
		if value < 0:
			limity = 0
		else:
			limity = 7
		if x is None or y is None:
			x, y = self.x, self.y

		if not self.queen:
			#RIGHT KILL
			if x < 6 and y is not limity-value and y is not limity:
				if bo[y+value][x+1] == -value and bo[y+value*2][x+2] == 0:
					self.moves.append(((x+2, y+value*2), (x+1, y+value), kills+1))
					self.posible_moves(bo, True, x+2, y+value*2, kills+1)
			#RIGHT
			if x < 7 and y is not limity and not rec:
				if bo[y+value][x+1] == 0:
					self.moves.append(((x+1, y+value), (-1, -1), kills))
			#LEFT KILL
			if x > 1 and y is not limity-value and y is not limity:
				if bo[y+value][x-1] == -value and bo[y+value*2][x-2] == 0:
					self.moves.append(((x-2, y+value*2), (x-1, y+value), kills+1))
					self.posible_moves(bo, True, x-2, y+value*2, kills+1)
			#LEFT
			if x > 0 and y is not limity and not rec:
				if bo[y+value][x-1] == 0:
					self.moves.append(((x-1, y+value), (-1, -1), kills))
		else:
			#TOP RIGHT
			if self.topr:
				tx, ty = x, y
				while tx < 7 and ty > 0:
					if bo[ty-1][tx+1] == 0:
						self.moves.append(((tx+1, ty-1), (-1, -1), kills))
					else:
						break
					tx += 1
					ty -= 1
				
			#TOP LEFT
			if self.topl:
				tx, ty = x, y
				while tx > 0 and ty > 0:
					if bo[ty-1][tx-1] == 0:
						self.moves.append(((tx-1, ty-1), (-1, -1), kills))
					else:
						break
					tx -= 1
					ty -= 1
			#DOWN RIGHT
			if self.downr:
				tx, ty = x, y
				while tx < 7 and ty < 7:
					if bo[ty+1][tx+1] == 0:
						self.moves.append(((tx+1, ty+1), (-1, -1), kills))
					else:
						break
					tx += 1
					ty += 1
			#DOWN LEFT
			if self.downl:
				tx, ty = x, y
				while tx > 0 and ty < 7:
					if bo[ty+1][tx-1] == 0:
						self.moves.append(((tx-1, ty+1), (-1, -1), kills))
					else:
						break
					tx -= 1
					ty += 1
			#TOP RIGHT KILL
			if self.toprk:
				tx, ty = x, y
				kill = 0
				while tx < 6 and ty > 1:
					if bo[ty-1][tx+1] is -value and bo[ty-2][tx+2] is 0:
						ttx, tty = tx+2, ty-2
						kill += 1
						cont = -1
						while ttx < 8 and tty > -1:
							obj = bo[tty][ttx]
							if obj is 0:
								self.moves.append(((ttx, tty), (ttx+cont, tty-cont), kills+kill))
								self.toprk = False
								self.downlk = False
								self.topl = False
								self.topr = False
								self.downl = False
								self.downr = False
								self.posible_moves(bo, True, ttx, tty, kills+1)
								self.toprk = True
								self.downlk = True
								self.topl = True
								self.topr = True
								self.downl = True
								self.downr = True
								cont -= 1
								ttx += 1
								tty -= 1
							elif obj is -value:
								tx, ty = ttx-1, tty+1
								break
							else:
								tx, ty = ttx+1, tty-1
								break
						if obj == 0:
							tx += 1
							ty -= 1
					elif bo[ty-1][tx+1] is -value and bo[ty-2][tx+2] is -value:
						break
					elif bo[ty-1][tx+1] is value:
						break
					else:
						tx += 1
						ty -= 1
			#TOP LEFT KILL
			if self.toplk:
				tx, ty = x, y
				kill = 0
				while tx > 1 and ty > 1:
					if bo[ty-1][tx-1] is -value and bo[ty-2][tx-2] is 0:
						ttx, tty = tx-2, ty-2
						kill += 1
						cont = -1
						while ttx > -1 and tty > -1:
							obj = bo[tty][ttx]
							if obj is 0:
								self.moves.append(((ttx, tty), (ttx-cont, tty-cont), kills+kill))
								self.toplk = False
								self.downrk = False
								self.topl = False
								self.topr = False
								self.downl = False
								self.downr = False
								self.posible_moves(bo, True, ttx, tty, kills+1)
								self.toplk = True
								self.downrk = True
								self.topl = True
								self.topr = True
								self.downl = True
								self.downr = True
								cont -= 1
								ttx -= 1
								tty -= 1
							elif obj is -value:
								tx, ty = ttx+1, tty+1
								break
							else:
								tx, ty = ttx-1, tty-1
								break
						if obj == 0:
							tx -= 1
							ty -= 1
					elif bo[ty-1][tx-1] is -value and bo[ty-2][tx-2] is -value:
						break
					elif bo[ty-1][tx-1] is value:
						break
					else:
						tx -= 1
						ty -= 1
			#DOWN RIGHT KILL
			if self.downrk:
				tx, ty = x, y
				kill = 0
				while tx < 6 and ty < 6:
					if bo[ty+1][tx+1] is -value and bo[ty+2][tx+2] is 0:
						ttx, tty = tx+2, ty+2
						kill += 1
						cont = -1
						while ttx < 8 and tty < 8:
							obj = bo[tty][ttx]
							if obj is 0:
								self.moves.append(((ttx, tty), (ttx+cont, tty+cont), kills+kill))
								self.toplk = False
								self.downrk = False
								self.topl = False
								self.topr = False
								self.downl = False
								self.downr = False
								self.posible_moves(bo, True, ttx, tty, kills+1)
								self.toplk = True
								self.downrk = True
								self.topl = True
								self.topr = True
								self.downl = True
								self.downr = True
								cont -= 1
								ttx += 1
								tty += 1
							elif obj is -value:
								tx, ty = ttx-1, tty-1
								break
							else:
								tx, ty = ttx+1, tty+1
								break
						if obj == 0:
							tx += 1
							ty += 1
					elif bo[ty+1][tx+1] is -value and bo[ty+2][tx+2] is -value:
						break
					
					elif bo[ty+1][tx+1] is value:
						break
					else:
						tx += 1
						ty += 1
			#DOWN LEFT KILL
			if self.downlk:
				tx, ty = x, y
				kill = 0
				while tx > 1 and ty < 6:
					if bo[ty+1][tx-1] is -value and bo[ty+2][tx-2] is 0:
						ttx, tty = tx-2, ty+2
						kill += 1
						cont = -1
						while ttx > -1 and tty < 8:
							obj = bo[tty][ttx]
							if obj is 0:
								self.moves.append(((ttx, tty), (ttx-cont, tty+cont), kills+kill))
								self.toprk = False
								self.downlk = False
								self.topl = False
								self.topr = False
								self.downl = False
								self.downr = False
								self.posible_moves(bo, True, ttx, tty, kills+1)
								self.toprk = True
								self.downlk = True
								self.topl = True
								self.topr = True
								self.downl = True
								self.downr = True
								cont -= 1
								ttx -= 1
								tty += 1
							elif obj is -value:
								tx, ty = ttx+1, tty-1
								break
							else:
								tx, ty = ttx-1, tty+1
								break
						if obj == 0:
							tx -= 1
							ty += 1
					elif bo[ty+1][tx-1] is -value and bo[ty+2][tx-2] is -value:
						break
					elif bo[ty+1][tx-1] is value:
						break
					else:
						tx -= 1
						ty += 1
			
						

						
					
	
	def select(self, screen, img, pos):
		screen.blit(img, pos)
	
	def draw(self, img, pos, screen):
		screen.blit(img, pos)
			
	def reset_moves(self):
		self.moves.clear()
