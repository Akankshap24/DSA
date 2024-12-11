X, Y = input().split()
X = int(X)
Y = int(Y)
perimeter = 2 * (X + Y)
if perimeter >= 1000:
    print("YES")
else:
    print("NO")