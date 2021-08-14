from constants import *


def getIndexClick(screenX, screenY):
	i = (screenX-50)//50
	j = (screenY-50)//50
	return i, j


def draw_rect(screen, bgC, fgC, x, y, w, h):
	pygame.draw.rect(screen, fgC,(x, y, w, h))
	pygame.draw.rect(screen, bgC,(x+1, y+1, w-2, h-2))


def text(screen, size, text, bg, fg, cx, cy):
	font = pygame.font.Font(FONT, size)
	text = font.render(text, True, fg, bg)
	textRect = text.get_rect()
	textRect.center = (cx, cy)
	screen.blit(text, textRect)


def drawPieces(board, screen):
	for row in board.board:
		for col in row:
			col.draw(screen)


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