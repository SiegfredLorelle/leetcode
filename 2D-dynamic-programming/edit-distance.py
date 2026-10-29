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

        prev_row = [idx for idx in range(len(word2), -1, -1)]

        for idx1 in range(len(word1) - 1, -1, -1):
            curr_row = [0] * len(word2) + [len(word1) - idx1]
            for idx2 in range(len(word2) - 1, -1, -1):

                # chars match (free), or start from the diagonal for a replace
                curr_row[idx2] = prev_row[idx2 + 1]

                # try delete, insert, and replace, and add the operation did
                if word1[idx1] != word2[idx2]:
                    # delete from word1
                    curr_row[idx2] = min(prev_row[idx2], curr_row[idx2])
                    # insert into word1
                    curr_row[idx2] = min(curr_row[idx2 + 1], curr_row[idx2])

                    # count the operation we just chose
                    curr_row[idx2] += 1

            prev_row = curr_row

        return prev_row[0]

