"""Number of Islands
Given an m x n 2D binary grid `grid` 
which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and 
is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])
        
        def dfs(row, col):
            if (row >= ROW_SIZE or col >= COL_SIZE or
                row < 0 or col < 0 or
                grid[row][col] == "0"):
                return

            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        numIslands = 0
        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if grid[row][col] == "0":
                    continue
                dfs(row, col)
                numIslands += 1
        return numIslands
