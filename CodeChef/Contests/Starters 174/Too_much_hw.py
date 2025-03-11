https://www.codechef.com/START174D/problems/HWFIN

def homework(X, Y):
    if X + (10 * Y) >= 100:
        print("YES")
    else:
        print("NO")

X, Y = map(int, input().split())

homework(X, Y)