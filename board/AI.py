from constants import *

"""
class AI:
    def __init__(self):
        pass

    def evaluate(board):
        
        
            Function to evaluate certain state
            Piece value: 10 + distance from start
            Queen value: 20
            Win value: 120
            :return: score
        
        scoreCOMP = 0
        scoreHUMAN = 0
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                val, queen = board[y][x].value, board[y][x].queen
                if val is COMP and queen:
                    scoreCOMP += 20
                elif val is COMP and not queen:
                    scoreCOMP += 10 + y
                elif val is HUMAN and queen:
                    scoreHUMAN += 20
                elif val is HUMAN and not queen:
                    scoreHUMAN += 10 + (7 - y)
        if scoreCOMP == 0:
            score = 120 * (-COMP)
        elif scoreHUMAN == 0:
            score = 120 * (-HUMAN)
        else:
            score = scoreCOMP - scoreHUMAN
        return score

    def wins(player, board):
        return len(calculate_moves(-player, board)) == 0

    def game_over(board):
    
        return wins(COMP, board) or wins(HUMAN, board)

    def minimax(board, depth, alpha, beta, player):
        if player == COMP:
            best = [-1, -1, -1, -1, [], -infinity]
        else:
            best = [-1, -1, -1, -1, [], +infinity]

        # Evaluate state at certain depth
        if depth == 0 or game_over(board):
            score = evaluate(board)
            return [-1, -1, -1, -1, [], score]

        # Calculate outcomes of each posible move recursibely
        moves = calculate_moves(player, board)
        for move in moves:
            ix, iy = move[0]
            to_kill = move[1]
            x, y = move[2]

            queen = board[iy][ix].queen

            make_move(board, ix, iy, x, y, to_kill, player)
            score = minimax(board, depth - 1, alpha, beta, -player)
            unmake_move(board, x, y, ix, iy, queen, to_kill, player)

            score[0], score[1], score[2], score[3], score[4] = ix, iy, x, y, to_kill
            # If computer turn it have to maximize if not minimize
            if player == COMP:
                if score[5] > best[5]:
                    best = score
                alpha = max(alpha, score[5])
                if beta <= alpha:
                    break
            else:
                if score[5] < best[5]:
                    best = score
                beta = min(beta, score[5])
                if beta <= alpha:
                    break
        return best
        """