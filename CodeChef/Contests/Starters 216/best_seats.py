T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    min_cost = float('inf')
    
    for i in range(N - 1):
        cost = A[i] + A[i+1]
        min_cost = min(min_cost, cost)
    
    print(min_cost)

