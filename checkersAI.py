import pygame
from math import inf as infinity
from random import choice
import time
from piece import Piece

#CONSTANTS
WIDTH = 500
HEIGHT = 500
FONT = 'freesansbold.ttf'

HUMAN = -1
COMP = +1
BOARD = [
	[Piece(0, 0, 1), Piece(1, 0, 0), Piece(2, 0, 1), Piece(3, 0, 0), Piece(4, 0, 1), Piece(5, 0, 0), Piece(6, 0, 1), Piece(7, 0, 0)],
	[Piece(0, 1, 0), Piece(1, 1, 1), Piece(2, 1, 0), Piece(3, 1, 1), Piece(4, 1, 0), Piece(5, 1, 1), Piece(6, 1, 0), Piece(7, 1, 1)],
	[Piece(0, 2, 1), Piece(1, 2, 0), Piece(2, 2, 1), Piece(3, 2, 0), Piece(4, 2, 1), Piece(5, 2, 0), Piece(6, 2, 1), Piece(7, 2, 0)],
	[Piece(0, 3, 0), Piece(1, 3, 0), Piece(2, 3, 0), Piece(3, 3, 0), Piece(4, 3, 0), Piece(5, 3, 0), Piece(6, 3, 0), Piece(7, 3, 0)],
	[Piece(0, 4, 0), Piece(1, 4, 0), Piece(2, 4, 0), Piece(3, 4, 0), Piece(4, 4, 0), Piece(5, 4, 0), Piece(6, 4, 0), Piece(7, 4, 0)],
	[Piece(0, 5, 0), Piece(1, 5,-1), Piece(2, 5, 0), Piece(3, 5,-1), Piece(4, 5, 0), Piece(5, 5,-1), Piece(6, 5, 0), Piece(7, 5,-1)],
	[Piece(0, 6,-1), Piece(1, 6, 0), Piece(2, 6,-1), Piece(3, 6, 0), Piece(4, 6,-1), Piece(5, 6, 0), Piece(6, 6,-1), Piece(7, 6, 0)],
	[Piece(0, 7, 0), Piece(1, 7,-1), Piece(2, 7, 0), Piece(3, 7,-1), Piece(4, 7, 0), Piece(5, 7,-1), Piece(6, 7, 0), Piece(7, 7,-1)],
]


#IMAGES
ORANGE = pygame.image.load('imgs\\orange.png')
BROWN = pygame.image.load('imgs\\brown.png')
ORANGEQ = pygame.image.load('imgs\\orangeQ.png')
BROWNQ = pygame.image.load('imgs\\brownQ.png')
SELECTED = pygame.image.load('imgs\\selected.png')
BOARD_IMG = pygame.image.load('imgs\\board.png')
PREV = pygame.image.load('imgs\\prev.png')

#COLORS
BLUE = pygame.Color('0x4363d8')
DARK_BLUE = pygame.Color('0x000075')
SOFT_BLUE = pygame.Color('0x46f0f0')
BACK = pygame.Color('0xf58231')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


"""
				DRAW FUNCTIONS
"""
def draw_rect(screen, bgC, fgC, x, y, w, h):
	pygame.draw.rect(screen, fgC,(x, y, w, h))
	pygame.draw.rect(screen, bgC,(x+1, y+1, w-2, h-2))
	
def text(screen, size, text, bg, fg, cx, cy):
	font = pygame.font.Font(FONT, size) 
	text = font.render(text, True, fg, bg) 
	textRect = text.get_rect()  
	textRect.center = (cx, cy)
	screen.blit(text, textRect)


def draw_pieces(screen, inv, board):
	if inv:
		tCOMP = -COMP
		tHUMAN = -HUMAN
	else:
		tCOMP = COMP
		tHUMAN = HUMAN
	for y, row in enumerate(board):
		for x, col in enumerate(row):
			if board[y][x].value == tCOMP and not board[y][x].queen:
				board[y][x].draw(ORANGE, (50+x*50, 50+y*50), screen)
				
			elif board[y][x].value == tHUMAN and not board[y][x].queen:
				board[y][x].draw(BROWN, (50+x*50, 50+y*50), screen)
				
			elif board[y][x].value == tCOMP and board[y][x].queen:
				board[y][x].draw(ORANGEQ, (50+x*50, 50+y*50), screen)
				
			elif board[y][x].value == tHUMAN and board[y][x].queen:
				board[y][x].draw(BROWNQ, (50+x*50, 50+y*50), screen)

def select_pieces(screen, list, board):
	for elem in list:
		x, y = elem
		board[y][x].select(screen, SELECTED, (50+x*50, 50+y*50))

"""
				BOARD FUNCTIONS
"""
def get_board_values(board):
	bo = []
	for y, row in enumerate(board):
		aux_list = []
		for x, col in enumerate(row):
			aux_list.append(board[y][x].value)
		bo.append(aux_list)
	return bo

def get_index_click(x, y):
	i = (x-50)//50
	j = (y-50)//50
	return i, j
	
def calculate_moves(SYM, board):
	moves = []
	temp_moves = []
	max_k = -1
	for y, row in enumerate(board):
		for x, col in enumerate(row):
			if board[y][x].value == SYM:
				board[y][x].posible_moves(get_board_values(board))
				for move in board[y][x].moves:
					if move[2] > max_k:
						max_k = move[2]
	if max_k == 0:
		for y, row in enumerate(board):
			for x, col in enumerate(row):
				if board[y][x].value == SYM:
					for move in board[y][x].moves:
						moves.append(( (x, y), [], move[0] ))
	else:
		for y, row in enumerate(board):
			for x, col in enumerate(row):
				if board[y][x].value == SYM:
					for move in board[y][x].moves:
						if move[2] == max_k:
							temp_moves.append((board[y][x].moves, (x, y)))
							break
		for temp_move in temp_moves:
			list = []
			temp_move, orig = temp_move
			for i, move in enumerate(temp_move):
				if move[2] is max_k:
					list.append(i)
			for i in list:
				aux = i
				kills = []
				while temp_move[aux][2] > 0:
					kills.append(temp_move[aux][1])
					if aux > 0:
						if temp_move[aux][2] == temp_move[aux-1][2]:
							aux -= 1
					if aux > 0:	
						aux-=1
					else:
						break
				moves.append((orig, kills, temp_move[i][0]))
			
	for y, row in enumerate(board):
		for x, col in enumerate(row):
			if board[y][x].value == SYM:
				board[y][x].reset_moves()
	return moves
	
def make_move(board, ix, iy, x, y, to_kill, SYM):
	board[y][x] = Piece(x, y, SYM)
	if board[iy][ix].queen is True:	
		board[y][x].queen = True
	board[iy][ix] = Piece(ix, iy, 0)
	
	for elem in to_kill:
		a, b = elem
		board[b][a] = Piece(a, b, 0)
	if y is 0 and SYM == HUMAN:
		board[y][x].queen = True
	if y is 7 and SYM == COMP:
		board[y][x].queen = True

def unmake_move(board, ix, iy, x, y, tx, ty, queen, to_revive, SYM):
	board[iy][ix] = Piece(ix, iy, 0)
	board[y][x] = Piece(tx, ty, SYM)
	board[y][x].queen = queen
	
	for elem in to_revive:
		a, b = elem
		board[b][a] = Piece(a, b, -SYM)
	
def wins(player, board):
	if len(calculate_moves(-player, board)) is 0:
		return True
	else:
		return False

def evaluate(board):
	scoreCOMP = 0
	scoreHUMAN = 0
	for y, row in enumerate(board):
			for x, col in enumerate(row):
				if board[y][x].value == 1:
					if board[y][x].queen:
						scoreCOMP += 20
					else:
						scoreCOMP += 10+y
				elif board[y][x].value == -1:
					if board[y][x].queen:
						scoreHUMAN += 20
					else:
						scoreHUMAN += 10+(7-y)
	if scoreCOMP == 0:
		score = -120
	elif scoreHUMAN == 0:
		score = 120
	else:
		score = scoreCOMP-scoreHUMAN
	return score
	
def game_over(board):
    return wins(COMP, board) or wins(HUMAN,board)

def minimax(board, depth, player):
	if player == COMP:
		best = [-1, -1, -1, -1, [], -infinity]  
	else:
		best = [-1, -1, -1, -1, [], +infinity]  
		
	if depth == 0 or game_over(board):
		score = evaluate(board)
		return [-1, -1, -1, -1, [], score] 
	
	moves = calculate_moves(player, board)
	for move in moves:
		ix, iy = move[0]
		to_kill = move[1]
		x, y = move[2]
		
		tx, ty = ix, iy
		
		make_move(board, ix, iy, x, y, to_kill, player)		
		score = minimax(board, depth-1, -player)
		unmake_move(board, x, y, ix, iy, tx, ty, board[ty][tx].queen,to_kill, player)
		
		score[0], score[1], score[2], score[3], score[4] = ix, iy, x, y, to_kill
		if player == COMP:
			if score[5] > best[5]:
				best = score  # max value
		else:
			if score[5] < best[5]:
				best = score  # min value
	return best

"""
			GAME LOOP
"""

def game_loop(screen, human_turn, inv, depth_max):
	running = True
	first_clik = False
	select_time = False
	list_sel = []
	board = BOARD[:]
	prev_board = []
	prev_board.append(BOARD[:])
	moves = calculate_moves(HUMAN, board)
	xC, yC = 0, 0
	while running:
		#PROCESS EVENTS
		txC, tyC = 0, 0
		x, y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				keep_playing = False
			if event.type == pygame.MOUSEBUTTONUP:
				xC, yC = pygame.mouse.get_pos()
				txC, tyC = xC, yC

		#UPDATE
		if human_turn:
			if game_over(board):
				running = False
			if txC > 450 and txC < 500 and tyC > 50 and tyC < 100 and len(prev_board) > 1:
				board = [row[:] for row in prev_board[-1]]
				prev_board.pop()
				list_sel.clear()
				moves = calculate_moves(HUMAN, board)
				for move in moves:
					if move[0] not in list_sel:
						list_sel.append(move[0])
			if xC > 50 and xC < 450 and yC > 50 and yC < 450:
				i, j = get_index_click(xC, yC)
				if board[j][i].value is HUMAN:
					list_sel.clear()
					ix, iy = 0, 0
					for move in moves:
						orig, kill, fin = move
						if (i, j) == orig:
							ix, iy = i, j
							if (ix, iy) not in list_sel:
								list_sel.append((ix, iy))
							if fin not in list_sel:
								list_sel.append(fin)
							first_clik = True
							select_time = True
				elif board[j][i].value is 0 and first_clik:
					for move in moves:
						orig, kill, fin = move
						if ((ix, iy), (i, j)) == (orig, fin):
							prev_board.append([row[:] for row in board])
							make_move(board, ix, iy, i, j, kill, HUMAN)
							prev = 1
							human_turn = False
							xC, yC = 0, 0
					first_clik = False
					select_time = False
					list_sel.clear()
					
				else:
					first_clik = False
					select_time = False
					list_sel.clear()
			else:
				select_time = True
				for move in moves:
					if move[0] not in list_sel:
						list_sel.append(move[0])
		else:
			if game_over(board):
				running = False
			else:
				copy = [row[:] for row in board]
				move = minimax(copy, depth_max, COMP)
				ix, iy, x, y, to_kill, score = move
				make_move(board, ix, iy, x, y, to_kill, COMP)
				moves = calculate_moves(HUMAN, board)
				human_turn = True
				time.sleep(0.5)

		#DRAW
		screen.fill(DARK_BLUE)
		screen.blit(BOARD_IMG,(50, 50))
		if select_time:
			select_pieces(screen, list_sel, board)
		if not human_turn:
			text(screen, 20, 'Thinking...', DARK_BLUE, WHITE, 250, 25)
		draw_pieces(screen, inv, board)
		screen.blit(PREV, (450, 50))
		pygame.display.flip()
		
"""
			MENU LOOP
"""

def options_loop(screen):
	running = True
	human = True
	inv = False
	depth = 2
	start = False
	bgColorY = DARK_BLUE
	bgColorN = BLUE
	while running:
		#PROCESS EVENTS
		x, y = pygame.mouse.get_pos()
		xC, yC = 0, 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				xC, yC = pygame.mouse.get_pos()
		#UPDATE
		if xC > 150 and xC < 250 and yC > 100 and yC < 180:
			human = True
		if xC > 250 and xC < 350 and yC > 100 and yC < 180:
			human = False
		if xC > 150 and xC < 250 and yC > 200 and yC < 280:
			inv = False
		if xC > 250 and xC < 350 and yC > 200 and yC < 280:
			inv = True
		if xC > 100 and xC < 175 and yC > 350 and yC < 400:
			depth = 2
		if xC > 175+75/2 and xC < 175+75/2+75 and yC > 350 and yC < 400:
			depth = 4
		if xC > 325 and xC < 400 and yC > 350 and yC < 400:
			depth = 6
		if xC > 200 and xC < 300 and yC > 425 and yC < 475:
			start = True
		#DRAW
		if running:
			screen.fill(BACK)
			text(screen, 25, 'Select:', BACK, DARK_BLUE, 250, 40)
			if human:
				draw_rect(screen, bgColorY, WHITE, 150, 100, 100, 80)
				draw_rect(screen, bgColorN, WHITE, 250, 100, 100, 80)
				
				text(screen, 20, '1st', bgColorY, WHITE, 200, 145)
				text(screen, 20, '2nd', bgColorN, WHITE, 300, 145)
			else:
				draw_rect(screen, bgColorN, WHITE, 150, 100, 100, 80)
				draw_rect(screen, bgColorY, WHITE, 250, 100, 100, 80)
				
				text(screen, 20, '1st', bgColorN, WHITE, 200, 145)
				text(screen, 20, '2nd', bgColorY, WHITE, 300, 145)
			if not inv:
				draw_rect(screen, bgColorY, WHITE, 150, 200, 100, 80)
				draw_rect(screen, bgColorN, WHITE, 250, 200, 100, 80)
			else:
				draw_rect(screen, bgColorN, WHITE, 150, 200, 100, 80)
				draw_rect(screen, bgColorY, WHITE, 250, 200, 100, 80)
			screen.blit(BROWN, (200-25, 240-25))
			screen.blit(ORANGE, (300-25, 240-25))
			
			text(screen, 25, 'Difficulty:', BACK, DARK_BLUE, 250, 320)
			if depth == 2:
				draw_rect(screen, bgColorY, WHITE, 100, 350, 75, 50)
				draw_rect(screen, bgColorN, WHITE, 175+75/2, 350, 75, 50)
				draw_rect(screen, bgColorN, WHITE, 325, 350, 75, 50)
				
				text(screen, 15, 'Easy', bgColorY, WHITE, 100+75/2, 375)
				text(screen, 15, 'Medium', bgColorN, WHITE, 175+75, 375)
				text(screen, 15, 'Hard', bgColorN, WHITE, 325+75/2, 375)
			elif depth == 4:
				draw_rect(screen, bgColorN, WHITE, 100, 350, 75, 50)
				draw_rect(screen, bgColorY, WHITE, 175+75/2, 350, 75, 50)
				draw_rect(screen, bgColorN, WHITE, 325, 350, 75, 50)
				
				text(screen, 15, 'Easy', bgColorN, WHITE, 100+75/2, 375)
				text(screen, 15, 'Medium', bgColorY, WHITE, 175+75, 375)
				text(screen, 15, 'Hard', bgColorN, WHITE, 325+75/2, 375)
			else:
				draw_rect(screen, bgColorN, WHITE, 100, 350, 75, 50)
				draw_rect(screen, bgColorN, WHITE, 175+75/2, 350, 75, 50)
				draw_rect(screen, bgColorY, WHITE, 325, 350, 75, 50)
				
				text(screen, 15, 'Easy', bgColorN, WHITE, 100+75/2, 375)
				text(screen, 15, 'Medium', bgColorN, WHITE, 175+75, 375)
				text(screen, 15, 'Hard', bgColorY, WHITE, 325+75/2, 375)
			
			draw_rect(screen, SOFT_BLUE, WHITE, 200, 425, 100, 50)
			text(screen, 21, 'Start', SOFT_BLUE, DARK_BLUE, 250, 450)
			
			if start:
				text(screen, 20, 'Loading...', BACK, DARK_BLUE, 375, 450)
				pygame.display.flip()
				game_loop(screen, human, inv, depth)
				running = False
			pygame.display.flip()


"""
			MENU LOOP
"""

def menu_loop(screen):
	running = True
	while running:
		#PROCESS EVENTS
		x, y = pygame.mouse.get_pos()
		xC, yC = 0, 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				xC, yC = pygame.mouse.get_pos()
		#UPDATE
		bgColorL = BLUE
		bgColorR = BLUE	
		if x > 75 and x < 250 and y > 75+150 and y < 250+100:
			bgColorL = DARK_BLUE
			
		if x > 275 and x < 425 and y > 75+150 and y < 250+100:
			bgColorR = DARK_BLUE
			
		if xC > 75 and xC < 250 and yC > 75+150 and yC < 250+100:
			options_loop(screen)
			running = False
		if xC > 275 and xC < 425 and yC > 75+150 and yC < 250+100:
			running = False
		
		#DRAW
		if running:
			screen.fill(BACK)
			draw_rect(screen, bgColorL, WHITE, 75, 250, 150, 100)
			draw_rect(screen, bgColorR, WHITE, 275, 250, 150, 100)

			text(screen, 20, 'Play', bgColorL, WHITE, 150, 300)
			text(screen, 20, 'Rules', bgColorR, WHITE, 350, 300)
			text(screen, 60, 'DAMAS', BACK, DARK_BLUE, 250, 100)
			
			pygame.display.flip()

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Damas')
	
	menu_loop(screen)
	
	"""board = [
		[Piece(0, 0, 0), Piece(1, 0, 0), Piece(2, 0, 0), Piece(3, 0, 0), Piece(4, 0, 0), Piece(5, 0, 0), Piece(6, 0, 0), Piece(7, 0, 0)],
		[Piece(0, 1, 0), Piece(1, 1, 0), Piece(2, 1, 0), Piece(3, 1, 0), Piece(4, 1, 0), Piece(5, 1, 0), Piece(6, 1, 0), Piece(7, 1, 0)],
		[Piece(0, 2, 0), Piece(1, 2, 0), Piece(2, 2, 0), Piece(3, 2, 0), Piece(4, 2, 0), Piece(5, 2, 0), Piece(6, 2, 0), Piece(7, 2, 0)],
		[Piece(0, 3, 0), Piece(1, 3, 0), Piece(2, 3, 0), Piece(3, 3, 0), Piece(4, 3, 0), Piece(5, 3, 0), Piece(6, 3, 0), Piece(7, 3, 0)],
		[Piece(0, 4, 0), Piece(1, 4, 0), Piece(2, 4, 1), Piece(3, 4, 0), Piece(4, 4, 0), Piece(5, 4, 0), Piece(6, 4, 0), Piece(7, 4, 0)],
		[Piece(0, 5, 0), Piece(1, 5, 0), Piece(2, 5, 0), Piece(3, 5, 0), Piece(4, 5, 0), Piece(5, 5, 0), Piece(6, 5, 0), Piece(7, 5, 0)],
		[Piece(0, 6,-1), Piece(1, 6, 0), Piece(2, 6, 0), Piece(3, 6, 0), Piece(4, 6, 0), Piece(5, 6, 0), Piece(6, 6, 0), Piece(7, 6, 0)],
		[Piece(0, 7, 0), Piece(1, 7, 0), Piece(2, 7, 0), Piece(3, 7, 0), Piece(4, 7, 0), Piece(5, 7, 0), Piece(6, 7, 0), Piece(7, 7, 0)],
	]
	copy = [row[:] for row in board]
	move = minimax(copy, 0, COMP)
	print(move)"""

	pygame.quit()

if __name__ == '__main__':
    main()