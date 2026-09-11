"""Longest Common Subsequence
Given two strings text1 and text2, 
return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without 
changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        prev_row = [0] * (len(text2) + 1)

        for text1_idx in range(len(text1) - 1, -1, -1):
            curr_row = [0] * (len(text2) + 1)
            for text2_idx in range(len(text2) - 1, -1, -1):

                if text1[text1_idx] == text2[text2_idx]:
                    curr_row[text2_idx] = prev_row[text2_idx + 1] + 1
                else:
                    curr_row[text2_idx] = max(
                        curr_row[text2_idx + 1], 
                        prev_row[text2_idx]
                    )

            prev_row = curr_row

        return prev_row[0]

