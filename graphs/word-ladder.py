"""Word Ladder
A transformation sequence from word beginWord to word endWord using a 
dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. 
Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence 
from beginWord to endWord, or 0 if no such sequence exists.
"""

from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Build the graph (pattern -> words)
        adjList = collections.defaultdict(list)
        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1:]
                adjList[pattern].append(word)

        # BFS on the graph to reach endWord
        visited = set([beginWord])
        queue = collections.deque([beginWord])
        res = 1
        while queue:
            for wordIdx in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for charIdx in range(len(word)):
                    pattern = word[:charIdx] + "*" + word[charIdx + 1:]
                    for neighborWord in adjList[pattern]:
                        if neighborWord in visited:
                            continue
                        visited.add(neighborWord)
                        queue.append(neighborWord)

            res += 1
        return 0