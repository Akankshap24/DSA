https://www.codechef.com/START178D/problems/FOODBAL

def dish(F1, P1, F2, P2):
    diff1 = abs(F1 - P1)
    diff2 = abs(F2 - P2)

    if diff1 < diff2:
        return "First"
    elif diff1 > diff2:
        return "Second"
    else:
        return "Both"

F1, P1, F2, P2 = map(int, input().split())

print(dish(F1, P1, F2, P2))
