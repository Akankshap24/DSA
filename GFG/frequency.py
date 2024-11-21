class Solution:
    def findFrequency(self, arr, x):
        count = 0
        for element in arr:
            if element == x:
                count += 1
        return count  