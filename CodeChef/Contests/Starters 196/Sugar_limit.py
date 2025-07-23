T = int(input())

for _ in range(T):
    N = int(input())
    t = list(map(int, input().split()))
    s = list(map(int, input().split()))

    best = 0

    for limit in range(101):
        total = 0
        for i in range(N):
            if s[i] <= limit and t[i] > 0:
                total += t[i]
        h = total - limit
        if h > best:
            best = h

    print(best)

