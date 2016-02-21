board = [[] for _ in range(8)]
for i in range(8):
    board[i] = raw_input().strip()

def check(board):
    # check the rows
    for i in range(8):
        if sum(1 for x in board[i] if x == '*') != 1:
            return "invalid"

    # check the columns
    for i in range(8):
        if sum(1 for j in range(8) if board[j][i] == '*') != 1:
            return "invalid"

    # check the left to right diagonals
    for i in range(15):
        c = 0
        r, j = max(0, (7 - i) - (i / 8)), (i / 8) * (i - 7)
        while 0 <= r < 8 and 0 <= j < 8:
            if board[r][j] == '*':
                c += 1
            r += 1
            j += 1
        if c > 1:
            return "invalid"

    # check the right to left diagonals
    for i in range(15):
        c = 0
        r, j = max(0, (7 - i) - (i / 8)), 7 - (i / 8 * (i - 7))
        while 0 <= r < 8 and 0 <= j < 8:
            if board[r][j] == '*':
                c += 1
            r += 1
            j -= 1
        if c > 1:
            return "invalid"
    return "valid"

print check(board)
