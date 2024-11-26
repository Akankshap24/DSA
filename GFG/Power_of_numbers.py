class Solution:
    def reverse_exponentiation(self, n):
        reverse_n = int(str(n)[::-1])
        return n ** reverse_n