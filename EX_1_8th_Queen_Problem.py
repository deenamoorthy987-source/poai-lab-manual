#Ex No: 01  IMPLEMENTATION OF 8-QUEENS PROBLEM USING BACKTRACKING SEARCH ALGORITHM 

def print_board(board, N):
    for row in board:
        print("".join(row))
    print()


def is_safe(board, row, col, N):
    # Check same row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, N):
    if col == N:
        return True

    for row in range(N):

        if is_safe(board, row, col, N):
            board[row][col] = 'Q'

            if solve(board, col + 1, N):
                return True

            board[row][col] = '.'

    return False


def n_queen(N):
    board = [['.' for _ in range(N)] for _ in range(N)]

    if solve(board, 0, N):
        print(f"\nSolution for {N}-Queens\n")
        print_board(board, N)
    else:
        print("No Solution Exists")


N = 12
n_queen(N)
