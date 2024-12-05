class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        p1 = 0
        p2 = len(arr) - 1
        
        while p1 < p2:
            sum = arr[p1] + arr[p2]
            if sum == target:
                return True
            elif sum < target:
                p1 += 1
            else:
                p2 -= 1
                
        return False