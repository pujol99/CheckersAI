import pygame, os
from piece.piece import Piece

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