T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print("1 0")
        print("0 1")
    else:
        for i in range(N):
            row = [(i + j) % N for j in range(N)]
            print(*row)

