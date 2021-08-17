from constants import *
from ui.uiObject import UiObject


class Button(UiObject):

    isSelected = False

    def __init__(self, x, y, width, height, content, property=None, value=None):
        super().__init__(x, y)
        self.width, self.height = width, height
        self.cx, self.cy = self.computeCenter()

        self.property = property
        self.value = value
        self.content = content

    def update(self, settings):
        # Select if his condition is matched
        if self.property:
            self.isSelected = (settings[self.property] == self.value)

    def onHover(self, x, y):
        self.bgColor = self.hover if self.insideX(x) and self.insideY(y) else self.background

    def isClicked(self, x, y):
        return self.insideX(x) and self.insideY(y)

    def insideY(self, y):
        return self.y < y < self.y + self.height

    def insideX(self, x):
        return self.x < x < self.x + self.width

    def draw(self, screen):
        screen.drawRect(self.getBg(), self.fgColor, self.x, self.y, self.width, self.height)
        if self.content:
            screen.drawText(20, self.content, self.getBg(), self.fgColor, self.cx, self.cy)

    def getBg(self):
        return self.selected if self.isSelected else self.bgColor

    def computeCenter(self):
        return self.x + int(self.width/2), self.y + int(self.height/2)


class MenuButton(Button):
    fgColor = WHITE
    background = SOFT_BLUE
    hover = DARK_BLUE
    selected = BLACK


class GameButton(Button):
    def onHover(self, x, y):
        pass

    def getBg(self):
        return None

    def draw(self, screen):
        if self.content:
            screen.drawImage(self.content, self.x, self.y)
