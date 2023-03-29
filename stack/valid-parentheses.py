"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Close parenthesis : open parenthesis
        close_to_open_brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for char in s:
            if char not in close_to_open_brackets:
                stack.append(char)
            elif stack and stack[-1] == close_to_open_brackets[char]:
                    stack.pop()
            else:
                return False

        return not stack



sol = Solution()
result = sol.isValid("([{}])")
print(result)