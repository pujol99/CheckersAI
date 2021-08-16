from ui.screen import Screen
from stages.menu import *
from stages.game import *


def main():
	pygame.init()
	screen = Screen(pygame.display.set_mode((WIDTH, HEIGHT)))
	pygame.display.set_caption('Damas')

	settings = Menu(screen).settings
	if settings["start"]:
		Game(screen, settings)


if __name__ == '__main__':
	main()
