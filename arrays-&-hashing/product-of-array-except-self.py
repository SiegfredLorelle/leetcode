"""
Product of Array Except Self

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and
without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        
        # Get the product of elements from left to right
        for index in range(0, len(nums) - 1):
            output[index + 1] = output[index] * nums[index]
        
        # Loop in reverse, from 2nd to last element to first
        # Solve the product by multiplying
        # the product on its left (in output list) and right (current number)
        current_num = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            output[index] = current_num * output[index]
            current_num *= nums[index]
        
        return output

sol = Solution()
result = sol.productExceptSelf([1,2,3,4])
print(result)
