import time
from math import inf as infinity
from ui.utils import *
from ui.screen import Screen
from stages.menu import *
from stages.game import *


def main():
	pygame.init()
	screen = Screen(pygame.display.set_mode((WIDTH, HEIGHT)))
	pygame.display.set_caption('Damas')

	Menu(screen)
	game_loop(screen)


if __name__ == '__main__':
	main()
