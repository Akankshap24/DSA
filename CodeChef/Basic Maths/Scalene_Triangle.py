# Given A, B, and C as the sides of a triangle, determine whether the triangle is scalene.

t = int(input())
while t > 0:
    a, b, c = map(int, input().split())
    if a != b and b != c and c != a:
        print("YES")
    else:
        print("NO")
    t -= 1
