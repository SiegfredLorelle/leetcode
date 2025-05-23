"""Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        firstStep = 1
        secondStep = 1

        for _ in range(n - 1):
            tmp = firstStep
            firstStep += secondStep
            secondStep = tmp
        return firstStep
