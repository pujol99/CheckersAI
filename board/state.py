

class State:
    def __init__(self):
        self.states = []
        
    def undo(self):
        return self.states.pop()

    def add(self, board):
        self.states.append(board)