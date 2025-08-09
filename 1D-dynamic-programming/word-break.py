"""Word Break
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be
reused multiple times in the segmentation.
"""


from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}

        def dfs(idx):
            if idx == len(s):
                return True
            if idx in mem:
                return mem[idx]
            
            for word in wordDict:
                if idx + len(word) > len(s):
                    continue
                if word == s[idx : idx + len(word)]:
                     if dfs(idx + len(word)):
                        mem[idx] = True
                        return True

            mem[idx] = False
            return False

        return dfs(0)

