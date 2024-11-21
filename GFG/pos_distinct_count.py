class Solution:
    def distinctCount(self, arr):
        posnum = set()
        for element in arr:
            if element > 0:
                posnum.add(element)
        return len(posnum)        
        