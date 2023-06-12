"""Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order 
is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 
1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, 
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        # Set the start or end as lowest
        if nums[start] <= nums[end]:
            lowest = nums[start]
        else:
            lowest = nums[end]

        # Use binary search
        while start <= end:
            middle = (start + end) // 2
            # If the middle is low, then check the left side 
            if nums[middle] < lowest:
                lowest = nums[middle]
                end = middle - 1
            # If the middle is high, then check the right side 
            else:
                start = middle + 1

        return lowest

sol = Solution()
result = sol.findMin(nums=[4,5,6,7,0,1,2])
print(result)