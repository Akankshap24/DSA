T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    A = (Y + X) // 2
    B = (Y - X) // 2
    print(A, B)

