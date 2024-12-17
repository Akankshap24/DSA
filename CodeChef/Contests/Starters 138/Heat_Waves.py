https://www.codechef.com/START138D/problems/HEATWAVE

input_line = input().strip()
strx,stry= input_line.split()
X = int(strx)
Y = int(stry)
if Y > X:
    print("YES")
else:
    print("NO")