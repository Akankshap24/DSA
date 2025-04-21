class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def fibon(n):
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = fibon(n-1) + fibon(n-2)
            return memo[n]
        
        return fibon(n)

    