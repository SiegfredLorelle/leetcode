"""Longest Increasing Subsequence
Given an integer array nums, 
return the length of the longest strictly increasing.
"""

from types import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       mem = {}

       for start in range(len(nums) - 1, -1, -1):
           max_lis = 1
           for end in range(start + 1, len(nums)):
               if nums[start] >= nums[end]:
                   continue

               max_lis = max(max_lis, mem.get(end, 1) + 1)

           mem[start] = max_lis


       return max(mem.values())
