import pygame

class Screen:
    def __init__(self, screen):
        self.screen = screen
        self.bgImage = None

    def renderBg(self):
        self.screen.blit(self.bgImage, (0, 0))

    def render(self):
        pygame.display.flip()
