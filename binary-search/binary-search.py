"""
Binary Search

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Check if num is within the range of the smallest and largest
        if target < nums[0] or target > nums[-1]:
            return -1

        left = 0
        right = len(nums) - 1

        # Implement binary search
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle

        return -1


sol = Solution()
result = sol.search(nums=[-1,0,3,5,9,12], target=9)
print(result)