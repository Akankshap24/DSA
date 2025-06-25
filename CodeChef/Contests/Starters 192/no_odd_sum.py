for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    C1 = A.count(1)
    C2 = A.count(2)
    
    if C1 % 2 == 0:
        print(min(C2, C1 //2))
    else:
        print(C2)