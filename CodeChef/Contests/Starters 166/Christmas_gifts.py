https://www.codechef.com/START166D/problems/WRAPGIFTS

T = int(input())
for i in range(T):
    H,L,W = map(int,input().split())
    area = 2 * (H * L + L * W + W * H)
    gifts = 1000 // area
    print(gifts)