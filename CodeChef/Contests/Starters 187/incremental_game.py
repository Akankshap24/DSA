T = int(input())
for _ in range(T):
    X,Y,K = map(int, input().split())
    max_s = max(X,Y)
    win = "Bob"
    for f in range(1, K+1):
        if X >= f:
            newX = X - f 
            if newX <= f and Y <= f:
                win = "Alice"
                break
        
        if Y >= f:
            newY = Y - f 
            if X <= f and  newY <= f:
                win = "Alice"
                break
            
        
    print(win)



