""" Subsets
Given an integer array nums of unique elements, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        SOLUTION USING DECISION TREE TO EITHER INCLUDE OR EXCLUDE NUMS 
        """
        # ans = []
        # subset = []
        # def dfs(i):
        #     if i >= len(nums):
        #         ans.append(subset.copy())
        #         return
            
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return ans

        """
        SOLUTION USING DECISION TREE TO EXPLORE ALL POSSIBLE SUBSETS
        """
        res = [[]]
        currSubset = []

        def dfs(start):
            for curr in range(start, len(nums)):
                currSubset.append(nums[curr])
                res.append(currSubset.copy())
                dfs(curr + 1)
                currSubset.pop()

        dfs(0)
        return res