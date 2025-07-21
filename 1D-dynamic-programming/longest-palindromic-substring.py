"""Longest Palindromic Substring
Given a string s, return the longest palndromic substring in s.
"""

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.resSize = 0
        
        def checkPalindrome(leftIdx, rightIdx):
            left = leftIdx
            right = rightIdx
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                currentSize = right - left + 1
                if currentSize > self.resSize:
                    self.resSize = currentSize
                    self.res = s[left:right + 1]
                right += 1
                left -= 1


        for idx in range(len(s)):
            # Check for odd palindrome
            checkPalindrome(idx, idx)
            # Check for even palindrome
            checkPalindrome(idx, idx + 1)
        return self.res
