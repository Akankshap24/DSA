#Write a program to find the remainder when an integer A is divided by an integer B.

for i in range(int(input())):
    A, B = map(int, input().split())
    print(A % B)