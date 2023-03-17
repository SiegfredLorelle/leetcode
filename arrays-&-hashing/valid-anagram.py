class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)
        
        if len(s_hash) != len(t_hash):
            return False

        for i in s_hash:
            if s_hash[i] != t_hash.get(i, 0):
                return False
        return True




sol = Solution()
result = sol.isAnagram("rat", "car")
print(result)