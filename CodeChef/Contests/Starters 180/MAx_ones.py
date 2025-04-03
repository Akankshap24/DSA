def Max_ones():
    T = int(input())
    
    for _ in range(T):
        N, K = map(int, input().split())
        S = list(input())
        ones = S.count('1')
        
        if K == 0 or ones == 0:
            print(ones)
        else:
            max_ones = ones
            
            for i in range(N-1):
                if S[i] == '0' and '1' in S[i+1:] and K > 0:
                    S[i] = '1'
                    K -= 1
                    max_ones += 1
            print(max_ones)

Max_ones()
