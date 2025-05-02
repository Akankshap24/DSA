#Basic maths# Store: Calculate total earnings based on chocolates sold and Chef's daily goal

t = int(input())

while t > 0:
    x, y = map(int, input().split())
    if y <= x:
        total_amount = y
    else:
        total_amount = x + 2 * (y - x)
    print(total_amount)
    t -= 1
