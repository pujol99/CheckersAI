import pygame


class Loop:
    settings = {
        "running": True,
        "isFirst": True,
        "difficulty": 2,
        "start": False,
        "play": False,
        "howTo": False,
        "prev": False,
        "again": False,
        "hint": False,
    }

    def __init__(self, screen):
        self.screen = screen

        self.mainLoop()

    def catchEvents(self):
        self.xClick, self.yClick = 0, 0
        self.xHover, self.yHover = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings['running'] = False
                self.settings['start'] = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.xClick, self.yClick = pygame.mouse.get_pos()

    def manageFrame(self):
        self.catchEvents()

        for object in self.screen.objects:
            object.update(self.settings)
            object.onHover(self.xHover, self.yHover)
            if object.isClicked(self.xClick, self.yClick):
                self.settings[object.property] = object.value

        self.screen.drawBg()
        self.renderPipeline()
        self.screen.render()

    def renderPipeline(self):
        self.screen.drawObjects()