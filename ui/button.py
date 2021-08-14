from ui.utils import *
from constants import *


class Button:
    bgColor = BACK
    fgColor = WHITE

    def __init__(self, x, y, width, height, content, screen):
        self.x = x
        self.y = y
        self.fx = x + width
        self.fy = y + height
        self.screen = screen
        self.content = content

    def onHover(self, mouseX, mouseY):
        if self.x < mouseX < self.fx and self.y < mouseY < self.fy:
            self.bgColor = BLACK
        else:
            self.bgColor = BACK

    def clicked(self, mouseX, mouseY):
        return self.x < mouseX < self.fx and self.y < mouseY < self.fy

    def draw(self):
        draw_rect(self.screen, self.bgColor, self.fgColor, 75, 250, 150, 100)
        if self.content:
            text(self.screen, 20, self.content, self.bgColor, self.fgColor, 150, 300)


class MenuButton(Button):
    bgColor = BACK
    fgColor = WHITE


class GameButton(Button):
    bgColor = BLUE
    fgColor = DARK_BLUE
