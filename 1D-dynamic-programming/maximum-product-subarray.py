"""Maximum Product Subarray
Given an integer array nums, find a subarray
that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with first element (handles single element arrays)
        res = nums[0]

        # Track max and min products of subarrays ending at current position
        # Start with 1 (multiplicative identity) so first element multiplies correctly
        currentMaximum = 1  # Max product ending at current position
        currentMinimum = 1  # Min product ending at current position (crucial for negatives!)

        for num in nums:
            # Store current max before we update it (since we need it for min calculation)
            tmp = num * currentMaximum

            # For the new maximum: choose the best of these 3 options:
            # 1. Start fresh with just current number (num)
            # 2. Extend previous max subarray (tmp = num * currentMaximum)
            # 3. Extend previous min subarray (num * currentMinimum)
            # This is key! A negative num times negative min becomes positive max
            currentMaximum = max(num, tmp, num * currentMinimum)

            # For the new minimum: choose the worst of the same 3 options
            # We need to track minimum because:
            # - It might become maximum when multiplied by a negative number
            # - Two negatives make a positive, so today's min could be tomorrow's max
            currentMinimum = min(num, tmp, num * currentMinimum)

            # Update global maximum if current position's max is better
            res = max(res, currentMaximum)

        return res
