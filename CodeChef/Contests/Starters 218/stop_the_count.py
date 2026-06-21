T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    ones = ans = 0

    for i in range(N):
        if S[i] == '1':
            ones += 1
        if ones > (i + 1 - ones):
            ans += 1

    print(ans)

    ##

