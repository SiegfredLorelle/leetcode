"""N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.

Each solution contains a distinct board configuration 
of the n-queens' placement, where 'Q' and '.' 
both indicate a queen and an empty space, respectively.
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        takenCols = set()
        takenPosiDiag = set()
        takenNegaDiag = set()

        def dfs(row):
            if row >= n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                # Skip if current position is attacked
                if (col in takenCols
                    or row + col in takenPosiDiag
                    or row - col in takenNegaDiag):
                    continue

                # Add the Queen and take note of the positions she attacks
                takenCols.add(col)
                takenPosiDiag.add(row + col)
                takenNegaDiag.add(row - col)
                board[row][col] = "Q"

                # Go to next row to find a position to the next queen
                dfs(row + 1)

                # Reset to previous state by 
                # removing queen and removing positions she attacks
                takenCols.remove(col)
                takenPosiDiag.remove(row + col)
                takenNegaDiag.remove(row - col)
                board[row][col] = "."

        dfs(0)
        return res