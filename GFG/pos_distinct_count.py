# Positive Distinct Count
# https://practice.geeksforgeeks.org/problems/positive-distinct-count/1
class Solution:
    def distinctCount(self, arr):
        posnum = set()
        for element in arr:
            if element > 0:
                posnum.add(element)
        return len(posnum)        
        