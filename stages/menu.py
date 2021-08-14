from ui.button import *
from stages.settings import Settings

class Menu:
    def __init__(self, screen):
        self.settings = Settings()
        self.screen = screen
        self.screen.bgImage = FRONTPAGE

        self.home()

    def catchEvents(self):
        self.xC, self.yC = 0, 0
        self.x, self.y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.settings.start = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.xC, self.yC = pygame.mouse.get_pos()

    def options(self):
        self.running = True
        start = False

        button1st = MenuButton(50, 150, 150, 100, '1st', self.screen)
        button2nd = MenuButton(300, 150, 150, 100, '2nd', self.screen)
        buttonEasy = MenuButton(100, 250, 100, 100, 'Easy', self.screen)
        buttonMedium = MenuButton(200, 250, 100, 100, 'Medium', self.screen)
        buttonDifficult = MenuButton(300, 250, 100, 100, 'Hard', self.screen)
        buttonStart = MenuButton(300, 450, 150, 100, 'Start', self.screen)

        while self.running:
            self.catchEvents()

            button1st.onHover(self.x, self.y)
            button2nd.onHover(self.x, self.y)
            buttonEasy.onHover(self.x, self.y)
            buttonMedium.onHover(self.x, self.y)
            buttonDifficult.onHover(self.x, self.y)
            buttonStart.onHover(self.x, self.y)

            if button1st.clicked(self.xC, self.yC):
                self.settings.isFirst = True
            if button2nd.clicked(self.xC, self.yC):
                self.settings.isFirst = False

            if buttonEasy.clicked(self.xC, self.yC):
                self.settings.difficulty = 2
            if buttonMedium.clicked(self.xC, self.yC):
                self.settings.difficulty = 4
            if buttonDifficult.clicked(self.xC, self.yC):
                self.settings.difficulty = 8

            if buttonStart.clicked(self.xC, self.yC):
                pygame.display.flip()
                running = False
            else:
                self.screen.renderBg()
                button1st.draw()
                button2nd.draw()
                buttonEasy.draw()
                buttonMedium.draw()
                buttonDifficult.draw()
                buttonStart.draw()
                self.screen.render()


    def home(self):
        self.running = True
        buttonStart = MenuButton(50, 300, 150, 100, 'Play', self.screen)
        buttonHelp = MenuButton(300, 300, 150, 100, 'How to play', self.screen)

        while self.running:
            self.catchEvents()

            buttonStart.onHover(self.x, self.y)
            buttonHelp.onHover(self.x, self.y)

            if buttonStart.clicked(self.xC, self.yC):
                self.options()
                self.running = False
            elif buttonHelp.clicked(self.xC, self.yC):
                self.running = False
            else:
                self.screen.renderBg()
                buttonHelp.draw()
                buttonStart.draw()
                self.screen.render()
