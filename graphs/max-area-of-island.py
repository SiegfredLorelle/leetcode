""" Max Area of Island
You are given an m x n binary matrix grid. 
An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])

        def dfs(row, col):
            if (row < 0 or row >= ROW_SIZE or
                col < 0 or col >= COL_SIZE or 
                not grid[row][col]):
                return 0
            
            grid[row][col] = 0

            topSize = dfs(row + 1, col)
            botSize = dfs(row - 1, col)
            rightSize = dfs(row, col + 1)
            leftSize = dfs(row, col - 1)

            return 1 + topSize + botSize + rightSize + leftSize

        res = 0
        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if not grid[row][col]:
                    continue
                res = max(dfs(row, col), res)
        return res
