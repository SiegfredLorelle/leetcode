"""Distinct Subsequences

Given two strings s and t, 
return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Dynamic Programming Bottom Up Approach
        # Time: O(m * n)
        # Space: O(n)
        prev_row = [0] * (len(t) + 1)
        prev_row[len(t)] = 1

        for s_idx in range(len(s) - 1, -1, -1):
            curr_row = [0] * (len(t) + 1)
            curr_row[len(t)] = 1
            for t_idx in range(len(t) - 1, -1, -1):
                curr_row[t_idx] = prev_row[t_idx]
                if s[s_idx] == t[t_idx]:
                    curr_row[t_idx] += prev_row[t_idx + 1]

            prev_row = curr_row

        return prev_row[0]


    # Dynamic Programming Top Down Approach with Caching
    # Time: O(m * n)
    # Space: O(m * n)
    # mem = {}

    # def dfs(s_idx, t_idx):
    #     if t_idx == len(t):
    #         return 1

    #     if s_idx >= len(s) or t_idx >= len(t):
    #         return 0

    #     key = (s_idx, t_idx)
    #     if key in mem:
    #         return mem[key]

    #     res = dfs(s_idx + 1, t_idx)
    #     if s[s_idx] == t[t_idx]:
    #         res += dfs(s_idx + 1, t_idx + 1)

    #     mem[key] = res
    #     return res


    # return dfs(0, 0)


