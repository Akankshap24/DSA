# Factorial of a number
# https://practice.geeksforgeeks.org/problems/factorial-of-a-number-1587115620/1
class Solution:
    def factorial (self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)