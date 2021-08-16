import pygame
import os

#CONSTANTS
WIDTH = 500
HEIGHT = 500
FONT = 'freesansbold.ttf'

#IMAGES
ORANGEP = pygame.image.load(os.path.abspath('imgs/orange.png'))
BROWNP = pygame.image.load(os.path.abspath('imgs/brown.png'))
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
WHITE = pygame.Color('0xffffff')
BLACK = pygame.Color('0x000000')