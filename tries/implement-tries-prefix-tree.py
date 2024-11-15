"""Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to 
efficiently store and retrieve keys in a dataset of strings. There are various 
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie 
    (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously 
    inserted string word that has the prefix prefix, and false otherwise.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                newNode = TrieNode()
                currNode.children[char] = newNode
            currNode = currNode.children[char]
        currNode.isEnd = True


    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True      


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)