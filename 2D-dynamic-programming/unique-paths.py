"""Unique Paths
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, 
return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

The test cases are generated so that 
the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic Programming (Bottom Up), spaced optimized O(n*m) O(n)
        old_row = [1] * n

        for y in range(m - 1):
            new_row = [1] * n
            for x in range(n - 1 - 1, -1, -1):
                new_row[x] = new_row[x + 1] + old_row[x]
            old_row = new_row

        return old_row[0]



    # Dynamic Programming (Top Down) with Memoization O(n*m) O(n*m)
        # mem = {}
        # def dfs(x, y):
        #     if x >= m or y >= n:
        #         return 0
        #     if x == m - 1 and y == n - 1:
        #         mem[(x, y)] = 1
        #         return mem[(x, y)]
        #     if (x, y) in mem:
        #         return mem[(x, y)]

        #     mem[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)
        #     return mem[(x, y)]


        # return dfs(0, 0)
