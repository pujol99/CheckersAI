import pygame


class Loop:
    def __init__(self, screen):
        self.screen = screen

        self.mainLoop()

    def catchEvents(self):
        self.xC, self.yC = 0, 0
        self.x, self.y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.settings.start = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.xC, self.yC = pygame.mouse.get_pos()