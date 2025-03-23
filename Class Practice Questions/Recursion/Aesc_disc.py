## Given N print all numbers from N, N-1....1, 1.....N-1 N 

def desc_asc(n):
    if n == 0:
        return
    print(n, end=" ")
    desc_asc(n-1)
    print(n, end=" ")

desc_asc(5)