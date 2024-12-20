# Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

n = int(input())
for i in range(n):
    a,b,c = sorted(map(int, input().split()))
    print(b)