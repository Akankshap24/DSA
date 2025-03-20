https://www.codechef.com/START177D/problems/BOX2

def boxes(x, y, k):
    diff = abs(x - y)
    
    if diff == k:
        return 0
    if (x + y) < k:
        return -1
    if diff % 2 != k % 2:
        return -1
    
    return abs(k - diff) // 2

T = int(input())  
for _ in range(T):
    x, y, k = map(int, input().split())
    print(boxes(x, y, k))