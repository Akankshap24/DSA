https://www.codechef.com/START166D/problems/MERRYXMAS

X = int(input())
count = 0 
 
if X >= 1:
    count += 1 
    X -= 1
if X >= 2:
    count += 1 
    X -= 2
if X >= 4:
    count += 1 
    X -= 4
print(count)
