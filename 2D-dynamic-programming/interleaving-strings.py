"""Interleaving String

Given strings s1, s2, and s3, 
find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where 
s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # # Dynamic Programming Bottom-up Approach
        # # Time: O(m * n)
        # # Space: O(n)

        S1_SIZE = len(s1)
        S2_SIZE = len(s2)

        # Early exit if s1 and s2 cannot from s3
        if S1_SIZE + S2_SIZE != len(s3):
            return False

        # Initialize 1st row of the dynamic programming grid
        prev_row = [False] * (S2_SIZE + 1)

        # Try each combination of s1 and s2
        # Initialize a new row for each character in s1
        for s1_idx in range(S1_SIZE, -1, -1):
            curr_row = [False] * (S2_SIZE + 1)
            for s2_idx in range(S2_SIZE, -1, -1):
                # When no character in s1 and s2 are used
                if s1_idx == S1_SIZE and s2_idx == S2_SIZE:
                    curr_row[s2_idx] = True

                s3_idx = s1_idx + s2_idx
                # Skip if no characters in s1 is used
                # Skip if currrent s1 char is not the same as current s3 char
                # Skip if previous s1 cannot form the rest of s3
                if s1_idx < S1_SIZE and s1[s1_idx] == s3[s3_idx] and prev_row[s2_idx]:
                    curr_row[s2_idx] = True

                # Skip if no characters in s2 is used
                # Skip if currrent s2 char is not the same as current s3 char
                # Skip if previous s2 cannot form the rest of s3
                if s2_idx < S2_SIZE and s2[s2_idx] == s3[s3_idx] and curr_row[s2_idx + 1]:
                    curr_row[s2_idx] = True


            prev_row = curr_row

        return prev_row[0]




        # # Dynamic Programming Top-down Approach
        # # Time: O(m * n)
        # # Space: O(m * n)

        # if len(s1) + len(s2) != len(s3):
        #     return False

        # mem = {}

        # def dfs(s1_idx, s2_idx, s3_idx):
        #     if s3_idx <= -1:
        #         if s1_idx != -1 and s2_idx != -1:
        #             return False
        #         return True

        #     key = (s1_idx, s2_idx)
        #     if key in mem:
        #         return mem[key]
        #    
        #     use_s1_path = False
        #     if s1_idx >= 0 and s3[s3_idx] == s1[s1_idx]:
        #         use_s1_path = dfs(s1_idx - 1, s2_idx, s3_idx - 1)


        #     use_s2_path = False
        #     if s2_idx >= 0 and s3[s3_idx] == s2[s2_idx]:
        #         use_s2_path = dfs(s1_idx, s2_idx - 1 , s3_idx - 1)

        #     mem[key] = use_s1_path or use_s2_path
        #     return mem[key]

        # return dfs(len(s1) - 1, len(s2) - 1, len(s3) - 1)



