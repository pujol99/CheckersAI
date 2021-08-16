from board.board import Board


class State:
    def __init__(self):
        self.states = []
        self.add(Board())

    def getCurrent(self):
        return self.states[-1]

    def undo(self):
        return self.states.pop()

    def add(self, board):
        self.states.append(board)
        return board