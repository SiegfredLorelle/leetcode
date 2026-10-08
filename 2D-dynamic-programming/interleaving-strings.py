"""
97. Interleaving String
Solved
Medium
Topics
premium lock iconCompanies

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

        if len(s1) + len(s2) != len(s3):
            return False

        mem = {}

        def dfs(s1_idx, s2_idx, s3_idx):
            if s3_idx <= -1:
                if s1_idx != -1 and s2_idx != -1:
                    return False
                return True

            key = (s1_idx, s2_idx)
            if key in mem:
                return mem[key]
           
            use_s1_path = False
            if s1_idx >= 0 and s3[s3_idx] == s1[s1_idx]:
                use_s1_path = dfs(s1_idx - 1, s2_idx, s3_idx - 1)


            use_s2_path = False
            if s2_idx >= 0 and s3[s3_idx] == s2[s2_idx]:
                use_s2_path = dfs(s1_idx, s2_idx - 1 , s3_idx - 1)

            mem[key] = use_s1_path or use_s2_path
            return mem[key]










        return dfs(len(s1) - 1, len(s2) - 1, len(s3) - 1)



