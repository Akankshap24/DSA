https://www.codechef.com/START172D/problems/SMLPAL

T = int(input())

for _ in range(T):
    X , Y = map(int, input().split())
    
    Z = "1" * (X//2) + "2" * (Y//2)
    
    sp = Z + Z [::-1]
    
    print(sp)