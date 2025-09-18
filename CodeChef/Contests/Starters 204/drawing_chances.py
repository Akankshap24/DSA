T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()
    count_A = S.count('1')
    count_B = S.count('0')
    r = N - M
    max_wins = max(count_A, count_B)
    min_wins = min(count_A, count_B)
    n = max_wins - min_wins
    if r >= n and (r - n) % 2 == 0:
        print("Yes")
    else:
        print("No")
