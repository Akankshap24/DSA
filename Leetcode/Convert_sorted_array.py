# Definition for a binary tree node.
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class Solution:
    def sortedArray(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        mid = len(nums) // 2
        return TreeNode(nums[mid],
                        self.sortedArray(nums[:mid]),
                        self.sortedArray(nums[mid+1:]))
