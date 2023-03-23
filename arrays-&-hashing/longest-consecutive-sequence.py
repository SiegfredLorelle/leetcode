"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        """ SOLUTION USING SORT """
        # nums = set(nums)

        # if len(nums) <= 1:
        #     return len(nums)

        # nums = sorted(nums)

        # res = 0
        # count = 1
        # for index in range(len(nums) - 1):
        #     if abs(nums[index] - nums[index + 1]) == 1:
        #         count += 1
        #     else:
        #         if count > res:
        #             res = count
        #         count = 1

        # if count > res:
        #     res = count
        # return res


        """ SOLUTION BY COUNTING SEQUENCES """
        nums = set(nums)

        if len(nums) <= 1:
            return len(nums)

        longest = 0
        for num in nums:
            # Check if starting sequence
            if num - 1 not in nums:
                    length = 1
                    while num + length in nums:
                        length += 1
                    
                    if longest < length:
                        longest = length 

        return longest
        



sol = Solution()
result = sol.longestConsecutive([100,4,200,1,3,2])
print(result)