from board.state import State
from ui.button import *
from ui.uiObject import *
from stages.loop import Loop


class Game(Loop):
    states = State()

    def mainLoop(self):
        self.isHumanTurn = self.settings["isFirst"]
        self.difficulty = self.settings["difficulty"]
        self.board = self.states.getCurrent()

        self.screen.objects = [
            Color(DARK_BLUE),
            Image(50, 50, BOARD_IMG),
            GameButton(100, 450, 0, 0, PREV, 'prev', True),
            GameButton(225, 450, 0, 0, HINT, 'hint', True),
            GameButton(350, 450, 0, 0, AGAIN, 'again', True)
        ]

        while self.settings["running"]:
            self.catchEvents()

            if self.isHumanTurn:
                self.humanTurn()
            else:
                self.aiTurn()

            self.manageFrame()

    def humanTurn(self):
        if self.board.turn:
            self.board.turn.doAction(self.xClick, self.yClick)
        else:
            self.isHumanTurn = False

    def aiTurn(self):
        print('AI turn')

    def renderPipeline(self):
        self.screen.drawObjects()
        self.screen.drawPieces(self.board)
