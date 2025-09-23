#Max Subarray
class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = float('-inf')

        for val in nums:
            curr_sum += val
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum
