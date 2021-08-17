

class UiObject:
    def __init__(self, x, y, isBg=False):
        self.disabled = False
        self.x, self.y = x, y
        self.isBg = isBg

    def enable(self):
        self.disabled = True

    def disable(self):
        self.disabled = False

    def update(self, settings):
        pass

    def onHover(self, x, y):
        pass

    def isClicked(self, x, y):
        pass


class Image(UiObject):

    def __init__(self, x, y, image, isBg=False):
        super().__init__(x, y, isBg)
        self.image = image

    def draw(self, screen):
        screen.drawImage(self.image, self.x, self.y)


class Color(UiObject):
    def __init__(self, color):
        self.color = color
        super().__init__(0, 0 ,True)

    def draw(self, screen):
        screen.drawColor(self.color)