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
    num_X = 0
    num_O = 0
    
    for line in board:
        for cell in line:
            if cell == "X":
                num_X+= 1
            elif cell == "O":
                num_O+= 1
    
    if num_X > num_O: 
        return "O"
    else:
        return "X"
  #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_plays = set()
    
    for i, line in enumerate(board):
        for j,  cell in enumerate(line):
            if cell == EMPTY:
                possible_plays.add((i, j))
    
    return possible_plays            
    
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_plays = actions(board)
    if action not in possible_plays:
        raise ValueError("Jogada Inválida")

    i, j = action
    new_board = board
    new_board[i][j] = player(board)
    return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
