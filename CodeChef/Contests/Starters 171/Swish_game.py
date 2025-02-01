https://www.codechef.com/problems/SWISHGAME

def solve():
    T = int(input())
    for _ in range(T):
        K, M = map(int,input().split())
        S = input().strip()
        
        swishCount = S.count("S")
                
        if swishCount >= M:
            print(K)
        else:
            re_swish = M - swishCount
            print(K + re_swish - 1)

solve()