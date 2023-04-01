"""
22. Generate Parentheses

Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def addParenthesis(current_combination, num_of_open, num_of_close):
            if num_of_open == n == num_of_close:
                combinations.append(current_combination)

            if num_of_open < n:
                addParenthesis(f"{current_combination}(", num_of_open + 1, num_of_close)
            if num_of_close < num_of_open:
                addParenthesis(f"{current_combination})", num_of_open, num_of_close + 1)
        

        combinations = []
        addParenthesis("(", 1, 0)
        return combinations



sol = Solution()
result = sol.generateParenthesis(3)
print(result)