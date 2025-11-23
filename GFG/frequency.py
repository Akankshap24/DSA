#Find the frequency of an element in an array
#https://practice.geeksforgeeks.org/problems/frequency-of-an-element-in-an-array-1587115620/1
class Solution:
    def findFrequency(self, arr, x):
        count = 0
        for element in arr:
            if element == x:
                count += 1
        return count  