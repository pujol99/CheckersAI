from constants import *


class Screen:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []

    def drawBg(self):
        for object in self.objects:
            if object.isBg:
                object.draw(self)

    def drawRect(self, bgC, fgC, x, y, w, h):
        pygame.draw.rect(self.screen, fgC, (x, y, w, h))
        pygame.draw.rect(self.screen, bgC, (x + 1, y + 1, w - 2, h - 2))

    def drawText(self, size, text, bg, fg, cx, cy):
        font = pygame.font.Font(FONT, size)
        text = font.render(text, True, fg, bg)
        textRect = text.get_rect()
        textRect.center = (cx, cy)
        self.screen.blit(text, textRect)

    def drawImage(self, img, x, y):
        self.screen.blit(img, (x, y))

    def drawColor(self, color):
        self.screen.fill(color)

    def drawPieces(self, board):
        for row in board.pieces:
            for col in row:
                col.draw(self.screen)

    def drawObjects(self):
        for object in self.objects:
            if not object.isBg:
                object.draw(self)

    def drawImages(self):
        for img in self.imgs:
            img.draw(self)

    def render(self):
        pygame.display.flip()


