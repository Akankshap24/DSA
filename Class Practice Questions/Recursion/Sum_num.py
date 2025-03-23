## Calculate and return the sum of n natural numbers.

def sum_natural_num(n):
    if n == 0:
        return 0
    return n + sum_natural_num(n-1)

print(sum_natural_num(5))