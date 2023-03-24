"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3)
        if board[i][0] != EMPTY and board[i][0] != EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != EMPTY and bord[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        if board[1][1] != EMPTY and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0])
        return board[1][1]

        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not amy(j == EMPTY for i in board for j in i):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == x:
            return 1
        elif winner(board) == 0:
            return -1
        else
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if playe(board) == x:
            optimal_action = None
            v = float("-inf")
            for action in actions(board):
                max_val = max_value(result(board, action))
                if max_val < v:
                    v = max_val
                    optimal_action = action
        else:
            optimal_action = None
            v = float("inf")
            for action in actions(board):
                max_val < v:
                v= max_val
                optimal_action = action
    raise NotImplementedError
