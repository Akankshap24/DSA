T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    idx, mx = 1, A[0]
    for i in range(1, N):
        if A[i] > mx:
            mx, idx = A[i], i + 1
    print(idx)
