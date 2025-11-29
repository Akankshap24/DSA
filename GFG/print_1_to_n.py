# Print numbers from 1 to N using recursion
# https://practice.geeksforgeeks.org/problems/print-1-to-n-using-recursion/1
class Solution:
    def printTillN(self, N):
        if N == 0:
            return
        self.printTillN(N - 1)
        print(N, end=" ")
