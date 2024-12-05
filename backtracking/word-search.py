from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_SIZE = len(board)
        COL_SIZE = len(board[0])
        WORD_SIZE = len(word)
        self.ans = False
        def dfs(wordIdx, row, col):
            if (self.ans 
                or (row < 0 or row >= ROW_SIZE)
                or (col < 0 or col >= COL_SIZE)
                or word[wordIdx] != board[row][col]):
                return
            
            wordIdx += 1
            if wordIdx == WORD_SIZE:
                self.ans = True
                return

            tmp = board[row][col] 
            board[row][col] = "!"
            dfs(wordIdx, row + 1, col)
            dfs(wordIdx, row - 1, col)
            dfs(wordIdx, row, col + 1)
            dfs(wordIdx, row, col - 1)
            board[row][col] = tmp

        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                dfs(0, row, col)
        
        return self.ans