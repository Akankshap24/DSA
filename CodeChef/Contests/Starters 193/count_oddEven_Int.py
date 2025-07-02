T = int(input())

for _ in range(T):
    N = int(input())
    odd = even = 0
    
    for i in range(1, N+1):
        if N % i == 0:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    print(odd,even)
