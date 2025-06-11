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

board3 = [["X", EMPTY, EMPTY],
            [EMPTY,  "X", EMPTY],
            ["O", EMPTY, EMPTY]]

print(player(board1))
print(player(board2))
print(player(board3))

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
                
print(actions(board1))
print(actions(board2))
print(actions(board3))

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

print(result(board1, (0,0)))
print(result(board2, (1,0)))
print(result(board3, (1,2)))