import pprint

def isSafe(board, x, y, n):

    # Check the column
    for row in range(x):
        if board[row][y] == 'Q':
            return False

    # Check upper-left diagonal
    row = x
    col = y

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    # Check upper-right diagonal
    row = x
    col = y

    while row >= 0 and col < n:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col += 1

    return True


def nQueen(board, x, n):

    # All queens have been placed
    if x >= n:
        return True

    # Try each column in the current row
    for col in range(n):

        if isSafe(board, x, col, n):

            board[x][col] = 'Q'

            # Recursively place the next queen
            if nQueen(board, x + 1, n):
                return True

            # Backtrack
            board[x][col] = ' '

    return False


n = int(input("Enter number of queens: "))

board = [[' ' for _ in range(n)] for _ in range(n)]

if nQueen(board, 0, n):
    pprint.pprint(board)
else:
    print("No Solution")