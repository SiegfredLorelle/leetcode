"""Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalindrome(left, right):
            numPalindromes = 0
            while True:
                # Check if in bounds
                if left < 0 or right >= len(s):
                    return numPalindromes
                # Check if palindrome
                if s[left] != s[right]:
                    return numPalindromes
                # Continue counting palindromes
                numPalindromes += 1
                left -= 1
                right += 1

        res = 0
        for idx in range(len(s)):
            # Count odd palindromes
            numOddPalindromes = checkPalindrome(idx, idx)
            # Count even palindromes
            numEvenPalindromes = checkPalindrome(idx, idx + 1)
            # Count all palindromes
            res += (numOddPalindromes + numEvenPalindromes)

        return res
