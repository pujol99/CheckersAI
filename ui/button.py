from ui.utils import *
from constants import *


class Button:
    def __init__(self, x, y, width, height, content, screen):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.cx, self.cy = self.computeCenter()

        self.screen = screen
        self.content = content

    def onHover(self, x, y):
        self.bgColor = self.hv if self.insideX(x) and self.insideY(y) else self.bg

    def clicked(self, x, y):
        return self.insideX(x) and self.insideY(y)

    def draw(self):
        draw_rect(self.screen.screen, self.bgColor, self.fgColor, self.x, self.y, self.width, self.height)
        if self.content:
            text(self.screen.screen, 20, self.content, self.bgColor, self.fgColor, self.cx, self.cy)

    def insideY(self, y):
        return self.y < y < self.y + self.height

    def insideX(self, x):
        return self.x < x < self.x + self.width

    def computeCenter(self):
        return self.x + int(self.width/2), self.y + int(self.height/2)


class MenuButton(Button):
    bg = ORANGE
    fgColor = WHITE
    hv = BLACK


class GameButton(Button):
    bg = BLUE
    fgColor = DARK_BLUE
    hv = BLACK
