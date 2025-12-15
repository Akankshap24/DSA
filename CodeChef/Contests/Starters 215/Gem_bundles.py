for _ in range(int(input())):
    R,B,G = map(int,input().split())
    b = min(R,B,G)
    print(10*b+3*(R+B+G-3*b))

