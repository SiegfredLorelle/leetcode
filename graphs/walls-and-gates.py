"""Walls and Gates 

You are given a m×n 2D grid initialized with these three possible values:
    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. 
        We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. 
If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""

import collections
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """ SOLUTION USING BFS ON EVERY CELL """
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2 ** 31 - 1

        def bfs(row, col):
            visited = set([(row, col)])
            queue = collections.deque([(row, col)])
            levels = 0
            while queue:
                levels += 1
                for _ in range(len(queue)):
                    currRow, currCol = queue.popleft()
                    for nextRow, nextCol in neighbors:
                        row = currRow + nextRow
                        col = currCol + nextCol
                        if (row < 0 or row >= ROW_SIZE or
                            col < 0 or col >= COL_SIZE or
                            grid[row][col] == -1 or
                            (row, col) in visited):
                            continue
                        if grid[row][col] == 0:
                            return levels
                        visited.add((row, col))
                        queue.append((row, col))
            return INF

        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if grid[row][col] == INF: 
                    grid[row][col] = bfs(row, col)
