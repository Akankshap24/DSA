def two_sum(arr, target):
    arr.sort()

    left,right = 0, len(arr) - 1 

    while left < right :
        sum = arr[left] + arr[right]

        if sum == target:
            return True 
        elif sum < target:
            left +=1
        else:
            right -= 1

    return False

# Test Cases
arr = [0, 1, 2, 3, 4]
target = -2

if two_sum(arr, target):
    print("True")
else:
    print("False")