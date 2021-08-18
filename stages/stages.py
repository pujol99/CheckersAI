from ui.screen import Screen
from stages.gameStages.start import *
from stages.gameStages.game import *


class Stages:
    def __init__(self):
        self.stages = []
        self.screen = None

        self.initialize()
        self.run()

    def initialize(self):
        pygame.init()
        pygame.display.set_caption('Damas')
        self.screen = Screen(pygame.display.set_mode((WIDTH, HEIGHT)))

        self.stages.append(
            Start(self.screen))

    def run(self):
        while self.stages:
            nextStage = self.currentStage().loop()
            if not nextStage:
                return

            self.stages.append(
                nextStage(self.screen))

    def prevStage(self):
        self.stages.pop()

    def currentStage(self):
        return self.stages[-1]
