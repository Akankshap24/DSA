def two_sum(arr, target):
    n = len(arr)
    for i in range (n):
        for j in range(i+1, n):
            if arr [i] + arr[j] == target:
                return True
    return False


# Test Case 1

arr = [ 5, 4, 3, 2, 1 ]
target = 6

if two_sum(arr, target):
    print(True)
else:
    print(False)


# Test Case 2

arr = [ 5, 4, 3, 2, 1 ]
target = 0

if two_sum(arr, target):
    print(True)
else:
    print(False)

