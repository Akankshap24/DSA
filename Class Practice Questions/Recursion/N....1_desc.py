## Given N print all numbers from N....1 in desc order.

def desc_num(n):
    if n == 0:
        return 
    print(n, end = " ")
    desc_num(n-1)

desc_num(5)
