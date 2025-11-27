# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
class Solution:
    def countPair (self, k, arr) : 
        left = 0
        right = len(arr) - 1
        count = 0
        
        while left < right:
            currSum = arr[left] + arr[right]
            if currSum == k:
                count += 1
                left += 1
                right -= 1
            
            elif currSum < k:
                left += 1
                
            else:
                right -= 1
            
        return count