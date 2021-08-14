from ui.button import *
from stages.loop import Loop


class Menu(Loop):
    settings = {
        "isFirst": True,
        "difficulty": 2,
        "start": True
    }
    bg = FRONTPAGE

    def options(self):
        self.running = True
        button1st = MenuButton(100, 150, 150, 70, '1st', 'isFirst', True)
        button2nd = MenuButton(250, 150, 150, 70, '2nd', 'isFirst', False)
        buttonEasy = MenuButton(100, 300, 100, 50, 'Easy', 'difficulty', 2)
        buttonMedium = MenuButton(200, 300, 100, 50, 'Medium', 'difficulty', 4)
        buttonDifficult = MenuButton(300, 300, 100, 50, 'Hard', 'difficulty', 8)
        buttonStart = MenuButton(200, 400, 100, 50, 'Start')
        buttons = [button1st, button2nd, buttonEasy, buttonMedium, buttonDifficult, buttonStart]

        while self.running:
            self.catchEvents()

            for button in buttons:
                button.update(self.settings)

            for button in buttons:
                button.onHover(self.x, self.y)

            if button1st.clicked(self.xC, self.yC):
                self.settings["isFirst"] = True
            if button2nd.clicked(self.xC, self.yC):
                self.settings["isFirst"] = False

            if buttonEasy.clicked(self.xC, self.yC):
                self.settings["difficulty"] = 2
            if buttonMedium.clicked(self.xC, self.yC):
                self.settings["difficulty"] = 4
            if buttonDifficult.clicked(self.xC, self.yC):
                self.settings["difficulty"] = 8

            if buttonStart.clicked(self.xC, self.yC):
                self.running = False
            else:
                self.screen.renderBg(self.bg)
                for button in buttons:
                    button.draw(self.screen.screen)
                self.screen.render()

    def mainLoop(self):
        self.running = True

        buttonStart = MenuButton(50, 300, 150, 100, 'Play')
        buttonHelp = MenuButton(300, 300, 150, 100, 'How to play')
        buttons = [buttonStart, buttonHelp]

        while self.running:
            self.catchEvents()

            for button in buttons:
                button.update(self.settings)

            for button in buttons:
                button.onHover(self.x, self.y)

            if buttonStart.clicked(self.xC, self.yC):
                self.options()
                self.running = False
            elif buttonHelp.clicked(self.xC, self.yC):
                self.running = False
            else:
                self.screen.renderBg(self.bg)
                for button in buttons:
                    button.draw(self.screen.screen)
                self.screen.render()
