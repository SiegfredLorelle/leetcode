"""
Longest Repeating Character Replacement

You are given a string s and an integer k. 
You can choose any character of the string and 
change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring 
containing the same letter you can get after performing the above operations.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 # left ptr of  the sliding window
        count = {} 
        max_length = 1
        max_freq = 1

        for i, char in enumerate(s):
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
                if count[char] > max_freq:
                    max_freq = count[char]
            # # OR use get function to handle edge cases
            # count[char] = count.get(char, 0) + 1
            # if count[char] > max_freq:
                # max_freq = count[char]
            # max_freq = count[char]
                
            while (i - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1

            substring_length = i - start + 1
            if substring_length > max_length:
                max_length = substring_length

        return max_length

sol = Solution()
result = sol.characterReplacement(s = "ABAB", k = 2)
print(result)