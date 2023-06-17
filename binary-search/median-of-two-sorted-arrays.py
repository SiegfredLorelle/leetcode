"""Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
from typing import List



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Swap the two lists to ensure that nums1 is the shortest
        m, n = len(nums1), len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            m, n = n, m

        total = m + n
        half = total // 2

        # Use binary search to the shorter list
        start = 0
        end = m - 1
        while True:
            nums1_middle_index = (start + end) // 2
            nums2_middle_index = half - nums1_middle_index - 2
            
            # Assign values for middle and middle next (also deals with edge cases)
            if nums1_middle_index < 0:
                nums1_middle = float("-inf")
            else:
                nums1_middle = nums1[nums1_middle_index]
            if nums1_middle_index + 1 >= len(nums1):
                nums1_middle_next = float("inf")
            else:
                nums1_middle_next = nums1[nums1_middle_index + 1]
            if nums2_middle_index < 0:
                nums2_middle = float("-inf")
            else:
                nums2_middle = nums2[nums2_middle_index]
            if nums2_middle_index + 1 >= len(nums2):
                nums2_middle_next = float("inf")
            else:
                nums2_middle_next = nums2[nums2_middle_index + 1]

            # Check if the left partition is valid
            if nums1_middle <= nums2_middle_next and nums2_middle <= nums1_middle_next:
                if nums1_middle < nums2_middle:
                    larger_middle = nums2_middle
                else:
                    larger_middle = nums1_middle
                if nums1_middle_next < nums2_middle_next:
                    smaller_middle_next = nums1_middle_next
                else:
                    smaller_middle_next = nums2_middle_next
                # odd
                if total % 2:
                    return smaller_middle_next
                # even
                else:
                    return (larger_middle + smaller_middle_next) / 2

            # Move the start/end pointers to adjust the middle appropriately
            elif nums1_middle > nums2_middle_next:
                end = nums1_middle_index - 1
            else:
                start = nums1_middle_index + 1



sol = Solution()
result = sol.findMedianSortedArrays(nums1g=[1,2], nums2=[3,4])
print(result)