"""
Valid Anagram

Given two strings s and t, return true 
if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ Solution using one hashmap """
        hash = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        for i in t:
            if i not in hash:
                return False
            hash[i] -= 1

        for i in hash:
            if hash[i] != 0:
                return False
        return True



        """ Solution using two hashmaps """
        # s_hash, t_hash = {}, {}

        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):
        #     s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
        #     t_hash[t[i]] = 1 + t_hash.get(t[i], 0)
        
        # if len(s_hash) != len(t_hash):
        #     return False

        # for i in s_hash:
        #     if s_hash[i] != t_hash.get(i, 0):
        #         return False
        # return True




sol = Solution()
result = sol.isAnagram("rat", "car")
print(result)