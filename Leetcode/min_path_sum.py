class Solution:
    def minPathSum(self, g):
        for i in range(len(g)):
            for j in range(len(g[0])):
                if i and j: g[i][j] += min(g[i-1][j], g[i][j-1])
                elif i: g[i][j] += g[i-1][j]
                elif j: g[i][j] += g[i][j-1]
        return g[-1][-1]

        