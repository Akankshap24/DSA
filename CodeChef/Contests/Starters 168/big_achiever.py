https://www.codechef.com/START168D/problems/BIG

t = int(input())

for _ in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    M = 0
    res = []

    for X in A:
        if X >= M:
            res.append(1)
            M = X 
        else:
            res.append(0)
    
    print(*res)


