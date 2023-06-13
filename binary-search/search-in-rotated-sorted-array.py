"""Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order 
(with distinct values).

Prior to being passed to your function, 
nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). 
For example, 
[0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle

            # Use different conditions based on which side middle is
            # Left side
            if nums[middle] >= nums[start]:
                if nums[middle] < target or nums[start] > target:
                    start = middle + 1
                else:
                    end = middle - 1
            
            # Right side
            else:
                if nums[middle] > target or nums[end] < target:
                    end = middle - 1
                else:
                    start = middle + 1
            
        return -1



sol = Solution()
result = sol.search(nums=[4,5,6,7,0,1,2], target=0)
print(result)