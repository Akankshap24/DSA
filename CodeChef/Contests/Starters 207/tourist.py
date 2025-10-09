T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    distances = [abs(A - X) + abs(B - Y) for X, Y in (map(int, input().split()) for _ in range(N))]
    print(min(distances))

