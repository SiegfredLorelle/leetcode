class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.trieRoot
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index >= len(word):
                return node.isEnd
            if word[index] == ".":
                for childNode in node.children.values():
                    if dfs(index + 1, childNode):
                        return True
            if word[index] in node.children:
                return dfs(index + 1, node.children[word[index]])
            else:
                return False
        ans = dfs(0, self.trieRoot)
        return ans 
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)