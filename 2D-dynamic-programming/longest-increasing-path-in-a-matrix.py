"""Longest Increasing Path in a Matrix
Given an m x n integers matrix, 
return the length of the longest increasing path in matrix.
From each cell, 
you can either move in four directions: left, right, up, or down. 
You may not move diagonally or 
move outside the boundary (i.e., wrap-around is not allowed).
"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        COL_SIZE = len(matrix[0])
        ROW_SIZE = len(matrix)
        NEXT_DIRECTIONS = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        mem = {}

        def dfs(row, col):

            key = (row, col)
            if key in mem:
                return mem[key]

            curr_res = 1
            for row_increment, col_increment in NEXT_DIRECTIONS:
                next_row = row + row_increment
                next_col = col + col_increment

                if next_col >= COL_SIZE:
                    continue
                if next_col < 0:
                    continue
                if next_row >= ROW_SIZE:
                    continue
                if next_row < 0:
                    continue

                if matrix[row][col] <= matrix[next_row][next_col]:
                    continue

                curr_res = max(
                    dfs(next_row, next_col) + 1, 
                    curr_res
                )


            mem[key] = curr_res
            return curr_res


        res = 1
        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                res = max(dfs(row, col), res)

        return res

