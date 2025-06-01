T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    odd= sum(A[i] for i in range(0, N, 2))   
    even = sum(A[i] for i in range(1, N, 2))  
    
    print(max(odd, even))
