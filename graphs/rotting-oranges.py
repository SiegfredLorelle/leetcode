from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.freshCount = 0
        rottens = collections.deque([])
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])

        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if grid[row][col] == 1:
                    self.freshCount += 1
                elif grid[row][col] == 2:
                    rottens.append((row, col))

        def spreadRot(row, col):
            if  (row < 0 or row >= ROW_SIZE or
                col < 0 or col >= COL_SIZE or
                grid[row][col] != 1):
                return
            grid[row][col] = 2
            rottens.append((row, col))
            self.freshCount -= 1

        minute = 0
        while rottens and self.freshCount:
            minute += 1
            for _ in range(len(rottens)):
                row, col = rottens.popleft()
                spreadRot(row + 1, col)
                spreadRot(row - 1, col)
                spreadRot(row, col + 1)
                spreadRot(row, col - 1)
        
        if not self.freshCount:
            return minute
        return -1
