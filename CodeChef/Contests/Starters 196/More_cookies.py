T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    for x in range(101): 
        alice = C + x
        if any(a < alice for a in A) and all(a != alice for a in A):
            print(x)
            break

