""" Subsets II
Given an integer array nums that may contain duplicates, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        currSubset = []
        nums.sort()

        def dfs(start):
            ans.append(currSubset.copy())

            for curr in range(start, len(nums)):
                if curr != start and nums[curr] == nums[curr - 1]:
                    continue
                
                currSubset.append(nums[curr])
                dfs(curr + 1)
                currSubset.pop()

        dfs(0)
        return ans
