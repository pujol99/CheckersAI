import pygame
from constants import *


class Screen:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []

    def drawBg(self, img):
        self.screen.blit(img, (0, 0))

    def drawRect(self, bgC, fgC, x, y, w, h):
        pygame.draw.rect(self.screen, fgC, (x, y, w, h))
        pygame.draw.rect(self.screen, bgC, (x + 1, y + 1, w - 2, h - 2))

    def drawText(self, size, text, bg, fg, cx, cy):
        font = pygame.font.Font(FONT, size)
        text = font.render(text, True, fg, bg)
        textRect = text.get_rect()
        textRect.center = (cx, cy)
        self.screen.blit(text, textRect)

    def drawPieces(self, board):
        for row in board.pieces:
            for col in row:
                col.draw(self.screen)

    def drawButton(self, btn):
        self.drawRect(btn.getBg(), btn.fgColor, btn.x, btn.y, btn.width, btn.height)
        if btn.content:
            self.drawText(20, btn.content, btn.getBg(), btn.fgColor, btn.cx, btn.cy)

    def drawButtons(self):
        for button in self.buttons:
            self.drawButton(button)


    def render(self):
        pygame.display.flip()


