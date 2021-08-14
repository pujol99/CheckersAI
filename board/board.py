import json
from piece.piece import Piece
from piece.black import Black
from piece.white import White
from piece.blackQueen import BlackQueen
from piece.whiteQueen import WhiteQueen
from piece.blank import Blank
from constants import *


class Board:
    def __init__(self):
        self.board = []

    def readFromJson(self, boardType):
        with open(f"./board/{boardType}.json") as json_file:
            data = json.load(json_file)

            for row, pieces in data.items():
                self.board.append([
                    pieceType(row, col, piece) for col, piece in enumerate(pieces)
                ])

            print(data)

    def invert(self):
        for row in self.board:
            row.reverse()
        self.board.reverse()


    def make_copy(self):
        """
            Makes an independent copy of a board
        """
        return [row[:] for row in self.board]

    def make_move(board, ix, iy, x, y, to_kill, SYM):
        """
            Place piece in new position and replace old one with a blank space
            If a top or bottom has been reach convert into queen
            Kill all the pieces in the list
        """
        board[y][x] = Piece(x, y, SYM)
        if board[iy][ix].queen is True:
            board[y][x].queen = True
        board[iy][ix] = Piece(ix, iy, 0)

        for elem in to_kill:
            a, b = elem
            board[b][a] = Piece(a, b, 0)

        if y == 0 and SYM == HUMAN:
            board[y][x].queen = True
        if y == 7 and SYM == COMP:
            board[y][x].queen = True

    def calculate_moves(SYM, board):
        """
            We will return all posible moves of a player
            The structure of the posible moves of a piece will be a list of tuples:
                (end, kills, nkills)
            And we will return a list of tuples:
            :return: (origen, kills_list, end)
        """
        # LOCAL VARIABLES
        moves = []
        temp_moves = []
        max_k = -1
        # Search which is the maxium kills with a single move we'll look all posible moves of a piece
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if board[y][x].value == SYM:
                    #board[y][x].posible_moves(get_board_values(board))
                    for move in board[y][x].moves:
                        end, kills, nkills = move
                        if nkills > max_k:
                            max_k = nkills
        # If the maxium is 0 simply pass all posible moves
        if max_k == 0:
            for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if board[y][x].value == SYM:
                        for move in board[y][x].moves:
                            end, kills, nkills = move
                            moves.append(((x, y), [], end))
        else:
            # If not we will look which pieces have the same kills move
            for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if board[y][x].value == SYM:
                        for move in board[y][x].moves:
                            end, kills, nkills = move
                            if nkills == max_k:
                                temp_moves.append((board[y][x].moves, (x, y)))
                                break
            # Each temp _move includes a tuple of posible moves of a piece and its origin
            # It figures it out the path of this high kill moves by backtracking the number of kills
            # Ex: (start1, kills, 1) <- (start2, kills, 2) <- (start3, kills, 3) x- (start4, kills, 2)
            # Result: (start1, kills, start3)
            for temp_move in temp_moves:
                # Create a list that will include the index of highest nkills
                list = []
                temp_move, orig = temp_move
                for i, move in enumerate(temp_move):
                    end, kill, nkills = move
                    if nkills is max_k:
                        list.append(i)
                # For each index of highest kill we go back until find a 1 kill move or end
                # If going back we find two equal nkills we dismiss one as it corresponds to another path
                for i in list:
                    aux = i
                    kills = []
                    # append move[aux] kill to the kill list
                    kills.append(temp_move[aux][1])
                    # While nkills is at least 1
                    while temp_move[aux][2] > 1 and aux > 0:
                        # If two equal consecutive nkills dismiss one
                        if temp_move[aux][2] == temp_move[aux - 1][2]:
                            aux -= 1
                        else:
                            aux -= 1
                            kills.append(temp_move[aux][1])
                    # Create the final move tuple with the origin kills end info
                    moves.append((orig, kills, temp_move[i][0]))

        # Reset posible moves of the pieces for next state
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if board[y][x].value == SYM:
                    board[y][x].reset_moves()

        return moves


def pieceType(row, col, id):
    if id == 1:
        return Black(row, col)
    if id == -1:
        return White(row, col)
    if id == 2:
        return BlackQueen(row, col)
    if id == -2:
        return WhiteQueen(row, col)
    else:
        return Blank(row, col)