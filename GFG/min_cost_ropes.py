import heapq
from typing import List

class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
    heapq.heapify(arr)
    cost = 0
    while len(arr) > 1:
        x = heapq.heappop(arr) + heapq.heappop(arr)
        cost += x
        heapq.heappush(arr,x)
    return cost