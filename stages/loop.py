import pygame


class Loop:
    def __init__(self, screen):
        self.screen = screen

        self.mainLoop()

    def catchEvents(self):
        self.xClick, self.yClick = 0, 0
        self.xHover, self.yHover = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.settings.start = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.xClick, self.yClick = pygame.mouse.get_pos()