"""Target Sum
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the 
symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.

For example, if nums = [2, 1], 
you can add a '+' before 2 and a '-' before 1 and 
concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, 
which evaluates to target.
"""


# # Time: O(n * m)
# # Space: O(n * m)
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        mem = {}

        def dfs(idx, curr_target):
            if idx == len(nums):
                if curr_target == 0:
                    return 1
                return 0

            if (key := (idx, curr_target)) in mem:
                return mem[key]


            minus_path = dfs(idx + 1, curr_target - nums[idx])
            add_path = dfs(idx + 1, curr_target + nums[idx])

            mem[key] = minus_path + add_path
            return mem[key]


        return dfs(0, target)
