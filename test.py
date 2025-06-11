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


    
EMPTY = None
    
board1 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board2 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY,  "X", EMPTY],
            [EMPTY, "O", EMPTY]]

board3 = [["X", "O", EMPTY],
            ["X",  "O", EMPTY],
            ["X", EMPTY, "O"]]
board4 = [["X", "X", EMPTY],
            ["O",  "O", "O"],
            ["X", EMPTY, "X"]]
board5 = [["X", "X", "O"],
            ["O",  "O", "X"],
            ["X", "X", "O"]]

#print(player(board1))
#print(player(board2))
#print(player(board3))

# actions
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
                
#print(actions(board1))
#print(actions(board2))
#print(actions(board3))

# result
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = board
    possible_plays = actions(board)
    if action not in possible_plays:
        raise ValueError("Jogada Inválida")

    i, j = action
    new_board[i][j] = player(board)
    return new_board

#print(result(board1, (0,0)))
#print(result(board2, (1,0)))
#print(result(board3, (1,2)))

# winner

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

print("winner ----")
print(winner(board1))
print(winner(board2))
print(winner(board3))
print(winner(board4))
print(winner(board5))

# terminal

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif any(EMPTY in row for row in board):
        return False
    else: return True

#print(terminal(board1))
#print(terminal(board2))
#print(terminal(board3))
#print(terminal(board4))
#print(terminal(board5))

# utility

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X": return 1
        elif winner(board) == "O": return -1
        else: return 0
    raise ValueError("Tabuleiro não está no estado terminal.")

#print(utility(board1))
#print(utility(board2))
#print(utility(board3))
#print(utility(board4))
#print(utility(board5))