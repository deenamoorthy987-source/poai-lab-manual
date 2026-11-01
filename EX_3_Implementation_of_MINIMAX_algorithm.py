#Ex No : 3 Implementation of MINIMAX Algorithm

#Tic-Tac-Toe Minimax Algorithm

PLAYER_X = 1
PLAYER_O = -1
EMPTY = 0

def evaluate(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return 0


def isMovesLeft(board):

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return True

    return False


def minimax(depth, board, is_max):

    score = evaluate(board)

    if score == PLAYER_X:
        return score

    if score == PLAYER_O:
        return score

    if not isMovesLeft(board):
        return 0

    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X

                    best = max(
                        best,
                        minimax(depth + 1, board, False)
                    )

                    board[i][j] = EMPTY

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O

                    best = min(
                        best,
                        minimax(depth + 1, board, True)
                    )

                    board[i][j] = EMPTY

        return best


def findBestMove(board):

    best_value = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:

                board[i][j] = PLAYER_X

                value = minimax(0, board, False)

                board[i][j] = EMPTY

                if value > best_value:
                    best_value = value
                    best_move = (i, j)

    return best_move


def printBoard(board):

    for row in board:
        for cell in row:

            if cell == PLAYER_X:
                print("X", end=" ")

            elif cell == PLAYER_O:
                print("O", end=" ")

            else:
                print(".", end=" ")

        print()


board = [
    [EMPTY, PLAYER_X, PLAYER_O],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, PLAYER_O, PLAYER_X]
]

print("Current Board\n")

print(board)

move = findBestMove(board)

print("\nBest Move:", move)

board[move[0]][move[1]] = PLAYER_X

print("\nBoard After AI Move\n")

printBoard(board)


#OUTPUT

#Sample Input:
#Enter 8 ternimal node value:
# 3 5 2 9 12 5 23 23 

#Sample Output:
#Optimal Value: 12
