"""
Valid Palindrome

A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ SOLUTION USING BUILT-IN FUNCTIONS """
        # s = [char for char in s.lower() if char.isalnum()]
        # # OR USE STRING INSTEAD OF LIST
        # # s = "".join(char for char in s.lower() if char.isalnum()) 
        # return s == s[::-1]




        """ SOLUTION USING ASCII CHARS (NO/LESS BUILT-IN FUNCTIONS) """
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.is_alpha_num(s[l]):
                l += 1
            while l < r and not self.is_alpha_num(s[r]):
                r -= 1
            if self.convert_to_lower(s[l]) != self.convert_to_lower(s[r]):
                return False
            l += 1
            r -= 1

        return True
            

    def is_alpha_num(self, ascii_val):
        return (
            ord("0") <= ord(ascii_val) <= ord("9") or
            ord("a") <= ord(ascii_val) <= ord("z") or
            ord("A") <= ord(ascii_val) <= ord("Z")
        )

    def convert_to_lower(self, s):
        if (ord("A") <= ord(s) <= ord("Z")):
            return chr(ord(s) + (ord("a") - ord("A")))
        return s



sol = Solution()
result = sol.isPalindrome("A man, a plan, a canal: Panama")
print(result)