"""
House Robber
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is 
that adjacent houses have security systems connected and 
it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money 
you can rob tonight without alerting the police.
"""

from typing import List 

class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums) 

        def dfs(idx):
            if idx >= len(nums):
                return 0
            if mem[idx] != -1:
                return mem[idx]

            firstOption = dfs(idx + 2)
            secondOption = dfs(idx + 3)
            maxMoney = nums[idx] + max(firstOption, secondOption)  
            mem[idx] = maxMoney
            return maxMoney

        return max(dfs(0), dfs(1))

