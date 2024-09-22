from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.isEnd = True
        currNode.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()
        ROW_SIZE = len(board)
        COL_SIZE = len(board[0])

        for word in words:
            trie.addWord(word)

        def dfs(i, j, node):
            if (0 > i or i >= ROW_SIZE 
                or 0 > j or j >= COL_SIZE
                or board[i][j] == "!"
                or board[i][j] not in node.children):
                return

            char = board[i][j]
            childNode = node.children[char]

            if childNode.word:
                ans.append(childNode.word)
                childNode.word = None

            board[i][j] = "!"
            dfs(i + 1, j, childNode)
            dfs(i - 1, j, childNode)
            dfs(i, j + 1, childNode)
            dfs(i, j - 1, childNode)
            board[i][j] = char

        
        for r in range(ROW_SIZE):
            for c in range(COL_SIZE):
                dfs(r, c, trie.root)

        return ans