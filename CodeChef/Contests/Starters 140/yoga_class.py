https://www.codechef.com/START140D/problems/YOGACLASS

T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    max_earnings = 0

    for k in range((N // 2) + 1):
        earnings = k * Y + (N - 2 * k) * X
        if earnings > max_earnings:
            max_earnings = earnings
    print(max_earnings)