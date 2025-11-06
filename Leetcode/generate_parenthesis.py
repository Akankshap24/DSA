## File: Leetcode/generate_parenthesis.py
## https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def back(s, o, c):
            if o == c == n: res.append(s); return
            if o < n: back(s+"(", o+1, c)
            if c < o: back(s+")", o, c+1)
        back("", 0, 0)
        return res