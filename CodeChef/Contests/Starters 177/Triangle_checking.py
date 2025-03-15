https://www.codechef.com/START177D/problems/TRICHECK

def triangle(A, B, C):
    if A + B > C and B + C > A and A + C > B:
        print("Yes")
    else:
        print("No")

A, B, C = map(int, input().split())

triangle(A, B, C)