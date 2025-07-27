"""Decode Ways
You have intercepted a secret message encoded as a string of numbers. 
The message is decoded via the following mapping:
"1" -> 'A'
"2" -> 'B'
...
"25" -> 'Y'
"26" -> 'Z'

However, while decoding the message,
you realize that there are many different ways you can decode the message 
because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:
    "AAJF" with the grouping (1, 1, 10, 6)
    "KJF" with the grouping (11, 10, 6)
    The grouping (1, 11, 06) is invalid 
        because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.
Given a string s containing only digits, 
return the number of ways to decode it. 
If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization array or cache
        mem = [-1] * len(s)
        
        def dfs(idx):
            # Check if valid decoding
            if idx >= len(s):
                return 1
            # Check if invalid decoding
            if s[idx] == "0":
                return 0
            # Check if already cached
            if mem[idx] != -1:
                return mem[idx]

            # Treat as solo digit
            oneDigit = dfs(idx + 1)

            # Check if possible to treat as two digits
            # Check if there is a next digit
            if idx == len(s) - 1:
                mem[idx] = oneDigit
                return mem[idx]
            # Check if two digit has a valid mapping (10-26 only)
            if not (s[idx] == "1" or
                s[idx] == "2" and s[idx + 1] not in "789"
            ):
                mem[idx] = oneDigit
                return mem[idx]

            # Treat as two digits
            twoDigit = dfs(idx + 2)
            mem[idx] = oneDigit + twoDigit
            return mem[idx]

        return dfs(0)
