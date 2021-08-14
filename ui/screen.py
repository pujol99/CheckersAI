import pygame

class Screen:
    def __init__(self, screen):
        self.screen = screen

    def renderBg(self, img):
        self.screen.blit(img, (0, 0))

    def render(self):
        pygame.display.flip()
