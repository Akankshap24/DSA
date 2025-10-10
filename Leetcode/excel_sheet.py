# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            res = chr(65 + n % 26) + res
            n //= 26
        return res
