class Solution:
    def solveNQueens(self, n: int):
        result = []
        cols, ld, rd = set(), set(), set()
        self.placeQueens(0, n, [], cols, ld, rd, result)
        return result

    def placeQueens(self, row, n, board, cols, ld, rd, result):
        if row == n:
            result.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
            return

        for col in range(n):
            if col in cols or (row - col) in ld or (row + col) in rd:
                continue

            board.append(col)
            cols.add(col)
            ld.add(row - col)
            rd.add(row + col)

            self.placeQueens(row + 1, n, board, cols, ld, rd, result)

            board.pop()
            cols.remove(col)
            ld.remove(row - col)
            rd.remove(row + col)

        