class Board(object):

    def __init__(self, rows, cols, row_sums, col_sums):
        self.rows = rows
        self.cols = cols
        self.row_sums = row_sums
        self.col_sums = col_sums
        assert self.rows == len(row_sums) and self.cols == len(col_sums)
        self.board = [[(None, None) for x in xrange(cols)] for y in xrange(rows)]

    def check_and_update_cell(self, r, c, op, rhs):
        cell = self.board[r][c]
        if op == "=":
            if cell[0] is None or cell[0] <= rhs:
                if cell[1] is None or cell[1] >= rhs:
                    self.board[r][c] = (rhs, rhs)
                    return True
            return False
        elif op == "<":
            if cell[0] is None or cell[0] < rhs:
                self.board[r][c] = (cell[0], min(cell[1], rhs - 1))
                return True
            return False
        elif op == ">":
            if cell[1] is None or cell[1] > rhs:
                self.board[r][c] = (max(cell[0], rhs + 1), cell[1])
                return True
            return False
        else:
            assert False, "unkown op: " + op

    def add_constraint(self, line):
        line = line.split()
        r, c, op, rhs = int(line[0]), int(line[1]), line[2], int(line[3])
        rows = [x for x in xrange(self.rows) if x == r or r == 0]
        cols = [x for x in xrange(self.cols) if x == c or c == 0]
        for r in rows:
            for c in cols:
                if not self.check_and_update_cell(r, c, op, rhs):
                    raise ValueError("Couldn't add constraint!")

    def finalize_board(self):
        # Validates each row and column with the row and column sum, raising exceptions along the way
        pass

    def print_board(self):
        # Prints out the board

        pass

N = int(raw_input())
for _ in xrange(N):
    raw_input()
    rows, cols = (int(x) for x in raw_input().split())
    row_sums = [int(x) for x in raw_input().split()]
    col_sums = [int(x) for x in raw_input().split()]
    board = Board(rows, cols, row_sums, col_sums)
    k = int(raw_input())
    try:
        for __ in xrange(k):
            board.add_constraint(raw_input())

        board.finalize_board()
        board.print_board()
    except ValueError:
        print "IMPOSSIBLE"

