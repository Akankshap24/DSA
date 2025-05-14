T = int(input())

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    
    redcount = C.count(1)
    bluecount = C.count(2)
    undeccount = C.count(0)
    
    if N % 2 == 1:
        print("No")
    else:
        morered = N // 2 - redcount
        print("Yes" if 0 <= morered <= undeccount else "No")