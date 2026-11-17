"""Edit Distance
Given two strings word1 and word2,
return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom Up Approach with 2D Dynamic Programming
        # Time: O(m*n)
        # Space: O(n)
        prev_row = [idx for idx in range(len(word2), -1, -1)]

        for word1_idx in range(len(word1) - 1, -1, -1):
            curr_row = [0] * len(word2) + [len(word1) - word1_idx]
            for word2_idx in range(len(word2) - 1, -1, -1):

                # If same char, no operation needed;
                # move to the next char in both words
                if word1[word1_idx] == word2[word2_idx]:
                    curr_row[word2_idx] = prev_row[word2_idx + 1]

                else:
                    curr_row[word2_idx] = min(
                        prev_row[word2_idx],         # Delete
                        curr_row[word2_idx + 1],     # Insert
                        prev_row[word2_idx + 1],     # Replace
                    ) + 1

            prev_row = curr_row

        return prev_row[0]

        # Top Down Approach using Recursion with Memoization
        # Time: O(m*n)
        # Space: O(m*n)
        # mem = {}
        #
        # def dfs(word1_idx, word2_idx):
        #     if word1_idx == len(word1):
        #         return len(word2) - word2_idx
        #     if word2_idx == len(word2):
        #         return len(word1) - word1_idx
        #
        #     key = (word1_idx, word2_idx)
        #     if key in mem:
        #         return mem[key]
        #
        #     if word1[word1_idx] == word2[word2_idx]:
        #         mem[key] = dfs(word1_idx + 1, word2_idx + 1)
        #     else:
        #         mem[key] = min(
        #             dfs(word1_idx + 1, word2_idx),      # Delete
        #             dfs(word1_idx, word2_idx + 1),      # Insert
        #             dfs(word1_idx + 1, word2_idx + 1),  # Replace
        #         ) + 1
        #
        #     return mem[key]
        #
        # return dfs(0, 0)

