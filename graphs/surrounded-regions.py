"""Surrounded Regions
You are given an m x n matrix board containing letters 'X' and 'O', 
capture regions that are surrounded:
    - Connect: A cell is connected to adjacent cells horizontally or vertically.
    - Region: To form a region connect every 'O' cell.
    - Surround: The region is surrounded with 'X' cells if 
    you can connect the region with 'X' cells and 
    none of the region cells are on the edge of the board.

To capture a surrounded region, 
replace all 'O's with 'X's in-place within the original board. 
You do not need to return anything.
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Legend:
        # - 'A': Marks an 'O' that is not connected to the edge (will become 'X')
        # - 'E': Marks an 'O' that is connected to the edge and should remain 'O'
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col):
            """DFS to mark 'O's connected to the edge as 'E'."""
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] not in "OA"):
                return
            board[row][col] = "E"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Do DFS for 'O's on the edges to mark them as 'E'
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] != "O"):
                    continue
                if (row == 0 or row == ROWS - 1 or
                    col == 0 or col == COLS - 1):
                    dfs(row, col)
                else:
                    board[row][col] = "A"

        # - Convert 'A' (captured 'O') to 'X'
        # - Convert 'E' (safe 'O') back to 'O'
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "A":
                    board[row][col] = "X"
                if board[row][col] == "E":
                    board[row][col] = "O"