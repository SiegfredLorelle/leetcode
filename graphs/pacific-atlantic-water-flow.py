"""Pacific Atlantic Water Flow
There is an m x n rectangular island that 
borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where 
heights[r][c] represents the height above sea level 
of the cell at coordinate (r, c).

The island receives a lot of rain, and 
the rain water can flow to neighboring cells 
directly north, south, east, and west if 
the neighboring cell's height is less than or equal to 
the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to 
both the Pacific and Atlantic oceans.
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        
        # Traverse neighboring water reachable to ocean
        def dfs(row, col, ocean, prevHeight):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                heights[row][col] < prevHeight or
                (row, col) in ocean):
                return

            ocean.add((row, col))
            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])

        # DFS on every water that directly neighbors an ocean
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0]) 
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1]) 
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS -1, col, atlantic, heights[ROWS - 1][col])

        return list(atlantic & pacific)