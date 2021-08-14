from constants import *
import pygame
from ui.utils import *
from ui.button import *
from settings import Settings

class Menu:
    def __init__(self, screen):
        self.settings = Settings()
        self.screen = screen

        self.home()

    def options(self, screen):
        # LOGIC DORS
        running = True
        start = False
        # PARAMETERS
        human = True
        inv = False
        depth = 2
        # LOCAL VARIABLES
        buttonStart = MenuButton(50, 150, 225, 100, 'Play', screen)
        buttonHelp = MenuButton(300, 150, 225, 100, 'How to play', screen)
        # LOOP
        while running:
            # PROCESS EVENTS
            xC, yC = 0, 0
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    xC, yC = pygame.mouse.get_pos()
            # UPDATE VALUES AND CONDITIONS
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
            if xC > 175 + 75 / 2 and xC < 250 + 75 / 2 and yC > 350 and yC < 400:
                depth = 4
            if xC > 325 and xC < 400 and yC > 350 and yC < 400:
                depth = 8

            if x > 200 and x < 300 and y > 425 and y < 475:
                bgColor = BLACK
            if xC > 200 and xC < 300 and yC > 425 and yC < 475:
                start = True
            # DRAW
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
                screen.blit(BROWN, (200 - 25, 290 - 25))
                screen.blit(ORANGE, (300 - 25, 290 - 25))

                if depth == 2:
                    draw_rect(screen, bgColorY, WHITE, 100, 350, 75, 50)
                    draw_rect(screen, bgColorN, WHITE, 175 + 75 / 2, 350, 75, 50)
                    draw_rect(screen, bgColorN, WHITE, 325, 350, 75, 50)

                    text(screen, 15, 'Easy', bgColorY, WHITE, 100 + 75 / 2, 375)
                    text(screen, 15, 'Medium', bgColorN, WHITE, 175 + 75, 375)
                    text(screen, 15, 'Hard', bgColorN, WHITE, 325 + 75 / 2, 375)
                elif depth == 4:
                    draw_rect(screen, bgColorN, WHITE, 100, 350, 75, 50)
                    draw_rect(screen, bgColorY, WHITE, 175 + 75 / 2, 350, 75, 50)
                    draw_rect(screen, bgColorN, WHITE, 325, 350, 75, 50)

                    text(screen, 15, 'Easy', bgColorN, WHITE, 100 + 75 / 2, 375)
                    text(screen, 15, 'Medium', bgColorY, WHITE, 175 + 75, 375)
                    text(screen, 15, 'Hard', bgColorN, WHITE, 325 + 75 / 2, 375)
                else:
                    draw_rect(screen, bgColorN, WHITE, 100, 350, 75, 50)
                    draw_rect(screen, bgColorN, WHITE, 175 + 75 / 2, 350, 75, 50)
                    draw_rect(screen, bgColorY, WHITE, 325, 350, 75, 50)

                    text(screen, 15, 'Easy', bgColorN, WHITE, 100 + 75 / 2, 375)
                    text(screen, 15, 'Medium', bgColorN, WHITE, 175 + 75, 375)
                    text(screen, 15, 'Hard', bgColorY, WHITE, 325 + 75 / 2, 375)

                draw_rect(screen, bgColor, WHITE, 200, 425, 100, 50)
                text(screen, 21, 'Start', bgColor, WHITE, 250, 450)

                if start:
                    text(screen, 20, 'Loading...', BLACK, WHITE, 375, 450)
                    pygame.display.flip()
                    game_loop(screen, human, inv, depth)
                    running = False
                pygame.display.flip()


    def home(self, screen):
        running = True
        buttonStart = MenuButton(50, 150, 225, 100, 'Play', screen)
        buttonHelp = MenuButton(300, 150, 225, 100, 'How to play', screen)
        while running:
            # PROCESS EVENTS
            x, y = pygame.mouse.get_pos()
            xC, yC = 0, 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    xC, yC = pygame.mouse.get_pos()
            # UPDATE VALUES AND CONDITIONS
            buttonStart.onHover(x, y)
            buttonHelp.onHover(x, y)

            if buttonStart.clicked(xC, yC):
                self.options(screen)
                running = False
            elif buttonStart.clicked(xC, yC):
                running = False
            else:
                screen.blit(FRONTPAGE, (0, 0))

                pygame.display.flip()