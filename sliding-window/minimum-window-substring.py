"""Minimum Window Substring

Given two strings s and t of lengths m and n respectively, 
return the minimum window 

substring of s such that every character in t (including duplicates) 
is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check for edge cases
        if len(s) < len(t):
            return ""

        # Count the characters in t by filling up the hashmap for t
        # Initialize the characters in t to be 0 for window hashmap
        t_count = {}
        window_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
            window_count[char] = 0

        start_index = 0
        min_window_indices, min_window_length = (-1, -1), float("infinity")
        num_of_matches, num_of_req_matches = 0, len(t_count)

        for i, char in enumerate(s, 1):
            # Fill up windows count
            if char in window_count:
                window_count[char] += 1

                # Check if the number of char in window matches in t
                if window_count[char] == t_count[char]:
                    num_of_matches += 1

                    while num_of_matches == num_of_req_matches:
                        # Update the indices of the minimum window
                        window_length = i - start_index
                        if window_length < min_window_length:
                            min_window_indices = (start_index, i)
                            min_window_length = window_length 

                        # Move the starting index of the sliding window
                        if s[start_index] in window_count: 
                            window_count[s[start_index]] -= 1
                            if window_count[s[start_index]] < t_count[s[start_index]]:
                                num_of_matches -= 1
                        start_index += 1

        if min_window_length == float("infinity"):
            return ""
        else:
            start_index, last_index = min_window_indices 
            return s[start_index : last_index]
        

sol = Solution()
result = sol.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(result)
