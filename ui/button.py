from ui.utils import *
from constants import *


class Button:

    isSelected = False

    def __init__(self, x, y, width, height, content, property=None, value=None):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.cx, self.cy = self.computeCenter()

        self.property = property
        self.value = value
        self.content = content

    def update(self, settings):
        if self.property:
            self.isSelected = (settings[self.property] == self.value)

    def onHover(self, x, y):
        self.bgColor = self.hv if self.insideX(x) and self.insideY(y) else self.bg

    def clicked(self, x, y):
        return self.insideX(x) and self.insideY(y)

    def insideY(self, y):
        return self.y < y < self.y + self.height

    def insideX(self, x):
        return self.x < x < self.x + self.width

    def getBg(self):
        return self.hv if self.isSelected else self.bgColor

    def computeCenter(self):
        return self.x + int(self.width/2), self.y + int(self.height/2)


class MenuButton(Button):
    bg = SOFT_BLUE
    fgColor = WHITE
    hv = BLACK


class GameButton(Button):
    bg = BLUE
    fgColor = DARK_BLUE
    hv = BLACK
