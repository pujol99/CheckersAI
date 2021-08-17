from ui.button import *
from ui.uiObject import *
from stages.loop import Loop


class Menu(Loop):

    def mainLoop(self):
        self.screen.objects = [
            Image(0, 0, FRONTPAGE, True),
            MenuButton(50, 300, 150, 100, 'Play', 'play', True),
            MenuButton(300, 300, 150, 100, 'How to play', 'howTo', True)]

        while not self.settings['play'] and not self.settings['howTo'] and self.settings['running']:
            self.manageFrame()

        if self.settings['play']:
            self.options()

    def options(self):
        self.screen.objects = [
            Image(0, 0, FRONTPAGE, True),
            MenuButton(100, 150, 150, 70, '1st', 'isFirst', True),
            MenuButton(250, 150, 150, 70, '2nd', 'isFirst', False),
            MenuButton(100, 300, 100, 50, 'Easy', 'difficulty', 2),
            MenuButton(200, 300, 100, 50, 'Medium', 'difficulty', 4),
            MenuButton(300, 300, 100, 50, 'Hard', 'difficulty', 8),
            MenuButton(200, 400, 100, 50, 'Start', 'start', True)]

        while not self.settings['start']:
            self.manageFrame()
