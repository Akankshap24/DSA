T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    for x in range(101): 
        ali = C + x
        if any(a < ali for a in A) and all(a != ali for a in A):
            print(x)
            break

