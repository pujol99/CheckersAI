from ui.button import *
from ui.uiObject import *
from stages.gameStages.loop import Loop
from stages.gameStages.menu import Menu


class Start(Loop):

    def init(self):
        self.settings["play"] = False
        self.settings["howTo"] = False

        self.screen.objects = [
            Image(0, 0, FRONTPAGE, True),
            MenuButton(50, 300, 150, 100, 'Play', 'play', True),
            MenuButton(300, 300, 150, 100, 'How to play', 'howTo', True)]

    def loop(self):
        while not self.settings['play'] and not self.settings['howTo'] and self.settings['running']:
            self.basicLoop()

        return self.finalize()

    def finalize(self):
        return Menu if self.settings['play'] else None

