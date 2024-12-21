## Given X 5-rupee coins, Y 10-rupee coins, and each chocolate costing Z rupees, find the maximum chocolates Chef can buy.

t = int(input())
while t > 0:
    x, y, z = map(int, input().split())
    money = 5 * x + 10 * y
    chocolates = money // z
    print(chocolates)
    t -= 1
