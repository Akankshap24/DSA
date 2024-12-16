https://www.codechef.com/START134D/problems/MONEYDOUBLE

def money_double(x, y):
    for i in range(y):
        if x * 2 >= x + 1000:
            x *= 2
        else:
            x += 1000
    return x  

T = int(input())

for i in range(T):
    x, y = input().split()
    x = int(x)
    y = int(y)
    