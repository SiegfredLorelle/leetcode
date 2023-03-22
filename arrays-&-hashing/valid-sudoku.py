"""
Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. 

Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain
the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but
is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

"""
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        row_count = defaultdict(set)
        col_count = defaultdict(set)
        sub_box_nums = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in row_count[r] or
                    board[r][c] in col_count[c] or
                    board[r][c] in sub_box_nums[r // 3, c // 3]):
                    return False
                else:
                    row_count[r].add(board[r][c])
                    col_count[c].add(board[r][c])
                    sub_box_nums[r // 3, c // 3].add(board[r][c])
        
        return True




sol = Solution()
result = sol.isValidSudoku(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
)

print(result)
