from board.state import State
from ui.button import *
from stages.loop import Loop


class Game(Loop):
    def __init__(self, screen, settings):
        self.isHumanTurn = settings["isFirst"]
        self.difficulty = settings["difficulty"]

        self.states = State()
        self.board = self.states.getCurrent()

        super(Game, self).__init__(screen)

    """
    behavoir:
        if human turn
        compute available pieces to move
        show available pieces to move
        wait for human to touch one of this pieces
            show available moves for that piece
                wait for human...
                make move
        
    """

    def mainLoop(self):
        self.running = True

        while self.running:
            self.catchEvents()

            if self.isHumanTurn:
                self.humanTurn()
            else:
                self.aiTurn()

            # DRAW
            self.screen.screen.fill(DARK_BLUE)
            self.screen.screen.blit(BOARD_IMG, (50, 50))
            self.screen.drawPieces(self.board)
            self.screen.screen.blit(PREV, (100, 450))
            self.screen.screen.blit(HINT, (225, 450))
            self.screen.screen.blit(AGAIN, (350, 450))
            self.screen.render()

    def humanTurn(self):
        if self.board.turn:
            self.board.turn.doAction(self.xC, self.yC)
        else:
            self.finishHumanTurn()

    def finishHumanTurn(self):
        self.isHumanTurn = False

    def aiTurn(self):
        print('AI turn')
