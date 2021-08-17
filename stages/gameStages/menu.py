from ui.button import *
from ui.uiObject import *
from stages.gameStages.loop import Loop
from stages.gameStages.game import Game


class Menu(Loop):

    def init(self):
        self.settings["isFirst"] = True
        self.settings["difficulty"] = 2
        self.settings["start"] = False

        self.screen.objects = [
            Image(0, 0, FRONTPAGE, True),
            MenuButton(100, 150, 150, 70, '1st', 'isFirst', True),
            MenuButton(250, 150, 150, 70, '2nd', 'isFirst', False),
            MenuButton(100, 300, 100, 50, 'Easy', 'difficulty', 2),
            MenuButton(200, 300, 100, 50, 'Medium', 'difficulty', 4),
            MenuButton(300, 300, 100, 50, 'Hard', 'difficulty', 8),
            MenuButton(200, 400, 100, 50, 'Start', 'start', True)]

    def loop(self):
        while not self.settings['start'] and self.settings['running']:
            self.basicLoop()

        return self.finalize()

    def finalize(self):
        return Game if self.settings['start'] else None




