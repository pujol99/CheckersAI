import pygame
from math import inf as infinity
import time
from piece import Piece
import os

#CONSTANTS
WIDTH = 500
HEIGHT = 500
FONT = 'freesansbold.ttf'

#BOARD INFO
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
ORANGE = pygame.image.load(os.path.abspath('imgs/orange.png'))
BROWN = pygame.image.load(os.path.abspath('imgs/brown.png'))
ORANGEQ = pygame.image.load(os.path.abspath('imgs/orangeQ.png'))
BROWNQ = pygame.image.load(os.path.abspath('imgs/brownQ.png'))
SELECTED_END = pygame.image.load(os.path.abspath('imgs/selected_end.png'))
SELECTED_KILL = pygame.image.load(os.path.abspath('imgs/selected_kill.png'))
SELECTED_ORIGN = pygame.image.load(os.path.abspath('imgs/selected_orign.png'))
BOARD_IMG = pygame.image.load(os.path.abspath('imgs/board.png'))
PREV = pygame.image.load(os.path.abspath('imgs/prev.png'))
HINT = pygame.image.load(os.path.abspath('imgs/hint.png'))
LAST = pygame.image.load(os.path.abspath('imgs/last.png'))
AGAIN = pygame.image.load(os.path.abspath('imgs/again.png'))
FRONTPAGE = pygame.image.load(os.path.abspath('imgs/frontpage.png'))

#COLORS
BLUE = pygame.Color('0x4363d8')
DARK_BLUE = pygame.Color('0x000075')
SOFT_BLUE = pygame.Color('0x46f0f0')
BACK = pygame.Color('0xf58231')
WHITE = pygame.Color('0xffffff')
BLACK = pygame.Color('0x000000')
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
	"""
		Draw all pieces inside a board, draw pieces depending of side
	"""
	#Set colors depending of player choice
	if inv:
		tCOMP = -COMP
		tHUMAN = -HUMAN
	else:
		tCOMP = COMP
		tHUMAN = HUMAN
	#Go through the board	
	for y, row in enumerate(board):
		for x, col in enumerate(row):
			if board[y][x].value == tCOMP and not board[y][x].queen:
				board[y][x].draw_piece(ORANGE, (50+x*50, 50+y*50), screen)
			elif board[y][x].value == tHUMAN and not board[y][x].queen:
				board[y][x].draw_piece(BROWN, (50+x*50, 50+y*50), screen)
			elif board[y][x].value == tCOMP and board[y][x].queen:
				board[y][x].draw_piece(ORANGEQ, (50+x*50, 50+y*50), screen)
			elif board[y][x].value == tHUMAN and board[y][x].queen:
				board[y][x].draw_piece(BROWNQ, (50+x*50, 50+y*50), screen)

def select_pieces(screen, list, board, col):
	"""
		Call pieces inside diferent lists to be selected
	"""
	for elem in list:
		x, y = elem
		board[y][x].select_piece(screen, col, (50+x*50, 50+y*50))

def clear_selections(lists):
	"""
		Clear all list of pieces that are being selected
	"""
	for list in lists:
		list.clear()

"""
				BOARD FUNCTIONS
"""
def get_board_values(board):
	"""
		Create board with only the values of the pieces
	"""
	return [[col.value for col in row] for row in board]
	
def make_copy(board):
	"""
		Makes an independent copy of a board
	"""
	return [row[:] for row in board]

def get_index_click(x, y):
	"""
		Gets a x, y position of the screen and returns the index of the board that aims
	"""
	i = (x-50)//50
	j = (y-50)//50
	return i, j
	
def calculate_moves(SYM, board):
	"""
		We will return all posible moves of a player
		The structure of the posible moves of a piece will be a list of tuples:
			(end, kills, nkills)
		And we will return a list of tuples:
		:return: (origen, kills_list, end)
	"""
	#LOCAL VARIABLES
	moves = []
	temp_moves = []
	max_k = -1
	#Search which is the maxium kills with a single move we'll look all posible moves of a piece
	for y, row in enumerate(board):
		for x, col in enumerate(row):
			if board[y][x].value == SYM:
				board[y][x].posible_moves(get_board_values(board))
				for move in board[y][x].moves:
					end, kills, nkills = move
					if nkills > max_k:
						max_k = nkills
	#If the maxium is 0 simply pass all posible moves
	if max_k is 0:
		for y, row in enumerate(board):
			for x, col in enumerate(row):
				if board[y][x].value == SYM:
					for move in board[y][x].moves:
						end, kills, nkills = move
						moves.append(((x, y), [], end))
	else:
		#If not we will look which pieces have the same kills move
		for y, row in enumerate(board):
			for x, col in enumerate(row):
				if board[y][x].value == SYM:
					for move in board[y][x].moves:
						end, kills, nkills = move
						if nkills == max_k:
							temp_moves.append((board[y][x].moves, (x, y)))
							break
		#Each temp _move includes a tuple of posible moves of a piece and its origin
		#It figures it out the path of this high kill moves by backtracking the number of kills
		#Ex: (start1, kills, 1) <- (start2, kills, 2) <- (start3, kills, 3) x- (start4, kills, 2) 
		#Result: (start1, kills, start3)
		for temp_move in temp_moves:
			#Create a list that will include the index of highest nkills
			list = []
			temp_move, orig = temp_move
			for i, move in enumerate(temp_move):
				end, kill, nkills = move
				if nkills is max_k:
					list.append(i)
			#For each index of highest kill we go back until find a 1 kill move or end
			#If going back we find two equal nkills we dismiss one as it corresponds to another path 
			for i in list:
				aux = i
				kills = []
				#append move[aux] kill to the kill list
				kills.append(temp_move[aux][1])
				#While nkills is at least 1
				while temp_move[aux][2] > 1 and aux > 0:
					#If two equal consecutive nkills dismiss one
					if temp_move[aux][2] == temp_move[aux-1][2]:
						aux -= 1
					else:
						aux -= 1
						kills.append(temp_move[aux][1])	
				#Create the final move tuple with the origin kills end info
				moves.append((orig, kills, temp_move[i][0]))

	#Reset posible moves of the pieces for next state	
	for y, row in enumerate(board):
		for x, col in enumerate(row):
			if board[y][x].value == SYM:
				board[y][x].reset_moves()

	return moves
	
def make_move(board, ix, iy, x, y, to_kill, SYM):
	"""
		Place piece in new position and replace old one with a blank space
		If a top or bottom has been reach convert into queen
		Kill all the pieces in the list
	"""
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

def unmake_move(board, ix, iy, x, y, queen, to_revive, SYM):
	"""
		:param ix, iy: piece that will return to original position
		:param x, y: piece that will be again occupied
		:param queen: know if was queen or not
	"""
	board[y][x] = Piece(x, y, SYM)
	board[y][x].queen = queen
	board[iy][ix] = Piece(ix, iy, 0)
	
	for elem in to_revive:
		a, b = elem
		board[b][a] = Piece(a, b, -SYM)

def evaluate(board):
	"""
		Function to evaluate certain state
		Piece value: 10 + distance from start
		Queen value: 20
		Win value: 120
		:return: score
	"""
	scoreCOMP = 0
	scoreHUMAN = 0
	for y, row in enumerate(board):
			for x, col in enumerate(row):
				val, queen = board[y][x].value, board[y][x].queen
				if val is COMP and queen:
					scoreCOMP += 20
				elif val is COMP and not queen:
					scoreCOMP += 10+y
				elif val is HUMAN and queen:
					scoreHUMAN += 20
				elif val is HUMAN and not queen:
					scoreHUMAN += 10+(7-y)
	if scoreCOMP == 0:
		score = 120*(-COMP)
	elif scoreHUMAN == 0:
		score = 120*(-HUMAN)
	else:
		score = scoreCOMP-scoreHUMAN
	return score

def wins(player, board):
	"""
		If enemy has no posible moves you've won
	"""
	return len(calculate_moves(-player, board)) is 0
	
def game_over(board):
	"""
		If someone wins game over
	"""
	return wins(COMP, board) or wins(HUMAN,board)

def minimax(board, depth, alpha, beta, player):
	"""
		Minimax algorithm used
	"""
	if player == COMP:
		best = [-1, -1, -1, -1, [], -infinity]  
	else:
		best = [-1, -1, -1, -1, [], +infinity]  
	
	#Evaluate state at certain depth
	if depth == 0 or game_over(board):
		score = evaluate(board)
		return [-1, -1, -1, -1, [], score] 
	
	#Calculate outcomes of each posible move recursibely
	moves = calculate_moves(player, board)
	for move in moves:
		ix, iy = move[0]
		to_kill = move[1]
		x, y = move[2]

		queen = board[iy][ix].queen
		
		make_move(board, ix, iy, x, y, to_kill, player)		
		score = minimax(board, depth-1, alpha, beta, -player)
		unmake_move(board, x, y, ix, iy, queen, to_kill, player)
		
		score[0], score[1], score[2], score[3], score[4] = ix, iy, x, y, to_kill
		#If computer turn it have to maximize if not minimize
		if player == COMP:
			if score[5] > best[5]:
				best = score
			alpha = max(alpha, score[5])
			if beta <= alpha:
				break
		else:
			if score[5] < best[5]:
				best = score
			beta = min(beta, score[5])
			if beta <= alpha:
				break
	return best

"""
			GAME LOOP
"""
def game_loop(screen, human_turn, inv, depth_max):
	#LOGIC DOORS
	running = True
	human_turn_copy = human_turn
	first_clik = False
	select_time = False
	hint_time = False
	#SELECTION LISTS
	kill_sel = []
	orign_sel = []
	end_sel = []
	last_sel = []
	#CREATE LOCAL COPIES OF BOARD
	board = make_copy(BOARD)
	prev_board = [make_copy(BOARD)]
	#LOCAL VARIABLES
	xC, yC = 0, 0
	txC, tyC = 0, 0
	
	if human_turn:
		moves = calculate_moves(HUMAN, board)
	#LOOP
	while running:
		#PROCESS EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				keep_playing = False
			if event.type == pygame.MOUSEBUTTONUP:
				xC, yC = pygame.mouse.get_pos()
				txC, tyC = xC, yC
		#UPDATE VALUES AND CONDITIONS
		if human_turn:
			#Check if PREV button was hitten
			if txC > 100 and txC < 150 and tyC > 450 and tyC < 500 and len(prev_board) > 1:
				hint_time = False
				select_time = True
				#Board is last saved version of itself and reload moves
				board = make_copy(prev_board.pop())

				moves = calculate_moves(HUMAN, board)
				#Reset variables
				xC, yC = 0, 0
				txC, tyC = 0, 0
				#Clear previous selections
				clear_selections([kill_sel, end_sel, orign_sel, last_sel])

			#Check if HINT button was hitten
			if txC > 225 and txC < 275 and tyC > 450 and tyC < 500:
				hint_time = True
				select_time = True
				#Get best move for this board copy
				copy = make_copy(board)
				move = minimax(copy, depth_max, -infinity, +infinity, HUMAN)
				ix, iy, x, y, to_kill, score = move
				#Reset variables
				xC, yC = 0, 0
				txC, tyC = 0, 0
				#Clear everything to show only best origin and end move
				clear_selections([kill_sel, end_sel, orign_sel, last_sel])
				orign_sel.append((ix, iy))
				end_sel.append((x, y))
			
			#Check if AGAIN button was hitten
			if txC > 350 and txC < 400 and tyC > 450 and tyC < 500:
				hint_time = False
				select_time = True
				human_turn = human_turn_copy
				#Board is last saved version of itself and reload moves
				board = make_copy(BOARD)
				prev_board = [make_copy(BOARD)]
				

				moves = calculate_moves(HUMAN, board)
				#Reset variables
				xC, yC = 0, 0
				txC, tyC = 0, 0
				#Clear previous selections
				clear_selections([kill_sel, end_sel, orign_sel, last_sel])

			#Check if BOARD PIECE was hitten
			if xC > 50 and xC < 450 and yC > 50 and yC < 450:
				hint_time = False
				select_time = True
				#Get index of the click
				i, j = get_index_click(xC, yC)
				#Check if OWN PIECE was hitten
				if board[j][i].value is HUMAN:
					clear_selections([kill_sel, end_sel, orign_sel, last_sel])
					ix, iy = 0, 0
					for move in moves:
						orig, kills, fin = move
						if (i, j) == orig:
							ix, iy = i, j
							if (ix, iy) not in orign_sel:
								orign_sel.append((ix, iy))
							for kill in kills:
								if kill not in kill_sel:
									kill_sel.append(kill)
							if fin not in end_sel:
								end_sel.append(fin)
							first_clik = True
							select_time = True
				#Check if BLANK PIECE was hitten and origin is decided
				elif board[j][i].value is 0 and first_clik:
					for move in moves:
						orig, kills, fin = move
						if ((ix, iy), (i, j)) == (orig, fin):
							prev_board.append(make_copy(board))
							make_move(board, ix, iy, i, j, kills, HUMAN)
							prev = 1
							human_turn = False
							#Check if game is over
							if game_over(board):
								running = False
							xC, yC = 0, 0
					first_clik = False
					select_time = False
					clear_selections([kill_sel, end_sel, orign_sel])
				#Check if ANY PIECE was hitten
				else:
					#Reset origin decision and select posible moves
					first_clik = False
					if not hint_time:
						for move in moves:
							if move[0] not in orign_sel:
								orign_sel.append(move[0])
			else:
				select_time = True
				#Reset origin decision and select posible moves
				first_clik = False
				if not hint_time:
					for move in moves:
						if move[0] not in orign_sel:
							orign_sel.append(move[0])
		#Computer turn		
		else:
			#Check if game is over
			if game_over(board):
				running = False
			else:
				#Calculate the best move for this state and make move
				copy = make_copy(board)
				move = minimax(copy, depth_max, -infinity, +infinity, COMP)
				ix, iy, x, y, to_kill, score = move
				make_move(board, ix, iy, x, y, to_kill, COMP)
				last_sel.append((ix, iy))
				#Reset moves for human
				moves = calculate_moves(HUMAN, board)
				human_turn = True
				#Check if game is over
				if game_over(board):
					running = False
				time.sleep(0.5)

		#DRAW
		screen.fill(DARK_BLUE)
		screen.blit(BOARD_IMG,(50, 50))
		if select_time:
			select_pieces(screen, orign_sel, board, SELECTED_ORIGN)
			select_pieces(screen, end_sel, board, SELECTED_END)
			select_pieces(screen, last_sel, board, LAST)
			select_pieces(screen, kill_sel, board, SELECTED_KILL)
		if not human_turn:
			text(screen, 20, 'Thinking...', DARK_BLUE, WHITE, 250, 25)
		draw_pieces(screen, inv, board)
		screen.blit(PREV, (100, 450))
		screen.blit(HINT, (225, 450))
		screen.blit(AGAIN, (350, 450))
		pygame.display.flip()
		
"""
			MENU LOOP
"""

def options_loop(screen):
	#LOGIC DORS
	running = True
	start = False
	#PARAMETERS
	human = True
	inv = False
	depth = 2
	#LOCAL VARIABLES
	bgColorY = DARK_BLUE
	bgColorN = BLUE
	#LOOP
	while running:
		#PROCESS EVENTS
		xC, yC = 0, 0
		x, y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				xC, yC = pygame.mouse.get_pos()
		#UPDATE VALUES AND CONDITIONS
		bgColor = BACK
		if xC > 150 and xC < 250 and yC > 150 and yC < 230:
			human = True
		if xC > 250 and xC < 350 and yC > 150 and yC < 230:
			human = False
			
		if xC > 150 and xC < 250 and yC > 250 and yC < 320:
			inv = False
		if xC > 250 and xC < 350 and yC > 250 and yC < 320:
			inv = True
			
		if xC > 100 and xC < 175 and yC > 350 and yC < 400:
			depth = 2
		if xC > 175+75/2 and xC < 250+75/2 and yC > 350 and yC < 400:
			depth = 4
		if xC > 325 and xC < 400 and yC > 350 and yC < 400:
			depth = 8
		
		if x > 200 and x < 300 and y > 425 and y < 475:
			bgColor = BLACK
		if xC > 200 and xC < 300 and yC > 425 and yC < 475:
			start = True
		#DRAW
		if running:
			screen.blit(FRONTPAGE, (0, 0))
			if human:
				draw_rect(screen, bgColorY, WHITE, 150, 150, 100, 80)
				draw_rect(screen, bgColorN, WHITE, 250, 150, 100, 80)
				
				text(screen, 20, '1st', bgColorY, WHITE, 200, 190)
				text(screen, 20, '2nd', bgColorN, WHITE, 300, 190)
			else:
				draw_rect(screen, bgColorN, WHITE, 150, 150, 100, 80)
				draw_rect(screen, bgColorY, WHITE, 250, 150, 100, 80)
				
				text(screen, 20, '1st', bgColorN, WHITE, 200, 190)
				text(screen, 20, '2nd', bgColorY, WHITE, 300, 190)
			
			if not inv:
				draw_rect(screen, bgColorY, WHITE, 150, 250, 100, 80)
				draw_rect(screen, bgColorN, WHITE, 250, 250, 100, 80)
			else:
				draw_rect(screen, bgColorN, WHITE, 150, 250, 100, 80)
				draw_rect(screen, bgColorY, WHITE, 250, 250, 100, 80)
			screen.blit(BROWN, (200-25, 290-25))
			screen.blit(ORANGE, (300-25, 290-25))
			
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
			
			draw_rect(screen, bgColor, WHITE, 200, 425, 100, 50)
			text(screen, 21, 'Start', bgColor, WHITE, 250, 450)
			
			if start:
				text(screen, 20, 'Loading...', BLACK, WHITE, 375, 450)
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
		#UPDATE VALUES AND CONDITIONS
		bgColorL = BACK
		bgColorR = BACK	
		if x > 75 and x < 250 and y > 75+150 and y < 250+100:
			bgColorL = BLACK
			
		if x > 275 and x < 425 and y > 75+150 and y < 250+100:
			bgColorR = BLACK
			
		if xC > 75 and xC < 250 and yC > 75+150 and yC < 250+100:
			options_loop(screen)
			running = False
		if xC > 275 and xC < 425 and yC > 75+150 and yC < 250+100:
			running = False
		
		#DRAW
		if running:
			screen.blit(FRONTPAGE, (0, 0))
			draw_rect(screen, bgColorL, WHITE, 75, 250, 150, 100)
			draw_rect(screen, bgColorR, WHITE, 275, 250, 150, 100)

			text(screen, 20, 'Play', bgColorL, WHITE, 150, 300)
			text(screen, 20, 'How to play', bgColorR, WHITE, 350, 300)
			
			pygame.display.flip()

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Damas')
	
	
	menu_loop(screen)	

if __name__ == '__main__':
    main()
