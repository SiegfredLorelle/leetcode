"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        substring = set(s[0])
        max_length = 1
        start_index = 0

        for char in s[1:]:
            while char in substring:
                substring.remove(s[start_index])
                start_index += 1

            substring.add(char)

            if len(substring) > max_length:
                max_length = len(substring)

        return max_length


sol = Solution()
result = sol.lengthOfLongestSubstring("abcabcbb")
print(result)