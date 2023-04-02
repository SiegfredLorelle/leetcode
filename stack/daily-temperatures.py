"""
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that 
answer[i] is the number of days 
you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, 
keep answer[i] == 0 instead.
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] # index of temps without ans yet

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i) 
        return res

sol = Solution()
result = sol.dailyTemperatures([73,74,75,71,69,72,76,73])
print(result)