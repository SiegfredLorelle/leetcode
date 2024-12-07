""" Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(start):
            if start >= len(s):
                res.append(path.copy())

            for current in range(start + 1, len(s) + 1):
                if not isPalindrome(start, current - 1):
                    continue
                path.append(s[start:current])
                dfs(current)
                path.pop()

        res = []
        path = []
        dfs(0)
        return res
