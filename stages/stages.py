from ui.screen import Screen
from stages.gameStages.start import *
from stages.gameStages.game import *


class GameStages:
    def __init__(self):
        self.stages = []
        self.screen = Screen(pygame.display.set_mode((WIDTH, HEIGHT)))

    def initialize(self):
        pygame.init()
        pygame.display.set_caption('Damas')
        self.stages.append(Start(self.screen))

    def run(self):
        nextStage = self.stages[-1].loop()
        if not nextStage:
            return

        self.stages.append(nextStage(self.screen))
        self.run()

    def prevStage(self):
        self.stages.pop()

