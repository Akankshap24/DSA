T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map (int, input().split()))
    
    count = 0 
    bh = arr[N - 1]
    
    for i in range(N - 1):
        if arr[i] < bh:
            count += 1
        else:
            break
        
            
    print(N - (count+1))
    
