def check(arr):
    total = sum(arr)
    if total >= 35:
        return 0
    arr.sort()
    coins = 0
    for i in range(5):
        if total >= 35:
            break
        total += 10 - arr[i]
        coins += 100
    return coins


T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    print(check(arr))