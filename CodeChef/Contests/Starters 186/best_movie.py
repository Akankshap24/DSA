T = int(input())

for _ in range(T):
    N = int(input())
    minCost = -1
    
    for _ in range(N):
        rating, cost = map(int, input().split())
        if rating >= 7:
            if minCost == -1 or cost < minCost:
                minCost = cost
                
    print(minCost)