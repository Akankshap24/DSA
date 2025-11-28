# Problem: Power of Numbers
# https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1
class Solution:
    def reverse_exponentiation(self, n):
        reverse_n = int(str(n)[::-1])
        return n ** reverse_n