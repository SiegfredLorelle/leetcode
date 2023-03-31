"""
Evaluate Reverse Polish Notation

You are given an array of strings tokens that 
represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. 
Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse 
    polish notation.
- The answer and all the intermediate calculations can be 
    represented in a 32-bit integer.
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = set(["+", "-", "/", "*"])
        stack = []

        for token in tokens:
            if token in operators:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    digit2, digit1 = stack.pop(), stack.pop()
                    stack.append(digit1 - digit2)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    digit2, digit1 = stack.pop(), stack.pop()
                    stack.append(int(digit1 / digit2))
            else:
                stack.append(int(token))
        
        return stack[0]



sol = Solution()
result = sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(result)