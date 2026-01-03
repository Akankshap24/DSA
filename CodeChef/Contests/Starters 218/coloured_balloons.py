T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    total_cost = 0
    for i in range(N):
        total_cost += (i + 1) * A[i]
    
    print(total_cost)

