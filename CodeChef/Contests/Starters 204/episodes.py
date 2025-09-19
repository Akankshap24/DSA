T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    total_minutes = N * K
    H = total_minutes // 60
    M = total_minutes % 60
    print(H, M)
