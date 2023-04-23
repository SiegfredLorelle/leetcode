"""Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Check for edges cases
        if len(s1) > len(s2):
            return False

        # Fill up a hash map for s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        # Fill up a hash map for s2
        left = 0
        s2_count = {}
        for i, char in enumerate(s2, 1):
            s2_count[char] = s2_count.get(char, 0) + 1
            
            # If the size of hash map for s2 is the same as 
            # the size of s1 then check if the s1 is in s2,
            # if not, then move the sliding window
            if i >= len(s1):
                if s2_count == s1_count:
                    return True
                else:
                    s2_count[s2[left]] -= 1
                    if not s2_count[s2[left]]:
                        s2_count.pop(s2[left])
                    left += 1
                
        return False


sol = Solution()
result = sol.checkInclusion(s1="ab", s2="eidbaooo")
print(result)
