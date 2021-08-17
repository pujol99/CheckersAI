from board.state import State
from ui.button import *
from ui.uiObject import *
from stages.gameStages.loop import Loop


class Game(Loop):
    states = State()
    board = states.getCurrent()

    def init(self):
        self.settings["prev"] = False
        self.settings["again"] = False
        self.settings["hint"] = False

        self.isHumanTurn = self.settings["isFirst"]

        self.screen.objects = [
            Color(DARK_BLUE),
            Image(50, 50, BOARD_IMG),
            GameButton(100, 450, PREV.get_width(), PREV.get_height(), PREV, 'prev', True),
            GameButton(225, 450, HINT.get_width(), HINT.get_height(), HINT, 'hint', True),
            GameButton(350, 450, AGAIN.get_width(), AGAIN.get_height(), AGAIN, 'again', True)
        ]

    def loop(self):
        while self.settings['running']:
            self.mainLoop()

        self.finalize()

    def mainLoop(self):
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
            self.finalize()

    def aiTurn(self):
        self.isHumanTurn = True

    def finalize(self):
        self.isHumanTurn = False
        self.board.clearAllMoves()
        self.board.unselectAll()
        self.board.initializeTurn()


    def renderPipeline(self):
        self.screen.drawObjects()
        self.screen.drawPieces(self.board)
