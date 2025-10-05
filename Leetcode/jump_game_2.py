# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jump = 0
        curr_end = 0
        far = 0

        for i in range(n - 1):  
            far = max(far, i + nums[i])
            if i == curr_end:
                jump += 1
                curr_end = far
                if curr_end >= n - 1:
                    break

        return jump
