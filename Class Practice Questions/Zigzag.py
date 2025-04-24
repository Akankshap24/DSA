class Solution:
    def con(self, s: str, nRows: int) -> str:
        if nRows == 1 or nRows >= len(s):
            return s

        rows = [''] * nRows
        i, step = 0, 1

        for char in s:
            rows[i] += char
            if i == 0:
                step = 1
            elif i == nRows - 1:
                step = -1
            i += step

        return ''.join(rows)

        