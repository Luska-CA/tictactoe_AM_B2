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
    # checando as linhas
    for line in board:
        if line[0] != EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    # checando colunas
    for column in range(3):
        if board[0][column] != EMPTY and board[0][column] == board[1][column] == board[2][column]:
            return board[0][column]
    # checando diagonais
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif EMPTY not in board:
        return True
    else: return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X": return 1
        elif winner(board) == "O": return -1
        else: return 0
    raise ValueError("Tabuleiro não está no estado terminal.")
   #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_atual = player(board)
    if terminal(board):
        return None
    
    if player_atual == "X":
        melhor_valor = -9999
        melhor_jogada = None
        for jogada in actions(board):
            novo_estado = result(board, jogada)
            valor = minvalue(novo_estado)
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_jogada = jogada
        return melhor_jogada
    
    else:
        melhor_valor = 9999
        melhor_jogada = None
        for jogada in actions(board):
            novo_estado = result(board, jogada)
            valor = maxvalue(novo_estado)
            if valor < melhor_valor:
                melhor_valor = valor
                melhor_jogada = jogada
        return melhor_jogada
    #raise NotImplementedError

def maxvalue(state): 
    if (terminal(state)):
      return utility(state)
    v = -9999
    for action in actions(state):
        v = max(v, minvalue(result(state,action)))
    return v

def minvalue(state):
    if terminal(state):
        return utility(state)
    v = 9999
    for action in actions(state):
        v = min(v, maxvalue(result(state, action)))
    return v
# CHECAR PÁGINA 288 DO SLIDE! Lá existe uma aplicação da função MINMAX