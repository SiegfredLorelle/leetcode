"""
Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [hash[complement], index]
            else:
                hash[num] = index


sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(result)