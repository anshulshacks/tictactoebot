"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def is_empty(board):
    for i in board:
        for j in i:
            if not j == EMPTY:
                return False
    return True

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if is_empty(board):
        return X
    x_count = 0
    o_count = 0
    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            elif j == O:
                o_count += 1


    if x_count > o_count:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.append([i, j])
    return possible_actions


def result(board, action):

    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = make_copy(board)

    new_board[action[0]][action[1]] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    full = True
    for i in board:
        for j in i:
            if j == None:
                full = False
    return winner(board) != None or full


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible = actions(board)

    best = possible[0]
    small = 2
    for action in possible:
        val = maxval(result(board, action))
        if val < small:
            small = val
            best = action

    return best
    #treat each action like the start of a different tree and then use the min or max value of the deepest node and assign to the head action and compare all the actions possible values.
    

def dfs(action, board):
    stack = [(board,action)]
    smallest = 2
    temp_board = board
    while not len(stack) == 0:
        combo = stack.pop()
        temp_act = combo[1]



        temp_board = result(combo[0].copy(), temp_act)
        if terminal(temp_board):
            smallest = min(smallest, utility(temp_board))
        else:
            new_actions = actions(temp_board)
            for a in new_actions:
                stack.append((temp_board, a))
    return smallest

def make_copy(board):
    dupe = initial_state()
    for i in range(3):
        for j in range(3):
            dupe[i][j] = board[i][j]
    return dupe

def maxval(state):
    if terminal(state):
        return utility(state)
    v = -100
    possible = actions(state)
    for action in possible:
        v = max(v, minval(result(state, action)))
    return v

def minval(state):
    if terminal(state):
        return utility(state)
    v = 100
    possible = actions(state)
    for action in possible:
        v = min(v, maxval(result(state, action)))
    return v


def print_board(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == None):
                print("   ", end="")
            else:
                print(" " + str(board[i][j]) + " ", end="")
            if (j < 2):
                print("|", end ="")

        if (i < 2):
            print("\n---+---+---")
    print("\n")

BOARD = initial_state()
# for i in range(0, 10):
#     print_board(BOARD)
#     # print(BOARD[0])
#     # print(BOARD[1])
#     # print(BOARD[2])
    
#     if i % 2 == 0:
#         row = int(input("Row: "))
#         col = int(input("Col: "))
#         arr = [row - 1, col - 1]
#         BOARD = result(BOARD, arr)
#     else:
#         board_copy = make_copy(BOARD)
#         board_copy[0][0] = X
#         best = minimax(BOARD)
#         BOARD = result(BOARD, best)

#     if (terminal(BOARD)):
#         print(winner(BOARD))
#         print_board(BOARD)

#         break
    