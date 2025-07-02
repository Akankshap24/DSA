A,B,C = map(int, input().split())

rectangle = A * B
square = C * C 

if rectangle == square:
    print("Yes")
else:
    print("No")

