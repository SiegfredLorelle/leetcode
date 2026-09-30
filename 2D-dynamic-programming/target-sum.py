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


class Solution:

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # # Time: O(n * m)
        # # Space: O(m)
        from collections import defaultdict

        prev_row = defaultdict(int)
        prev_row[0] = 1

        for num_idx in range(len(nums) - 1, -1, -1):
            new_row = defaultdict(int)
            for curr_target, res in prev_row.items():
                new_row[curr_target + nums[num_idx]] += res
                new_row[curr_target - nums[num_idx]] += res

            prev_row = new_row


        return prev_row.get(target, 0)


        # # Time: O(n * m)
        # # Space: O(n * m)
        #  mem = {}

        #  def dfs(idx, curr_target):
        #      if idx == len(nums):
        #          if curr_target == 0:
        #              return 1
        #          return 0

        #      if (key := (idx, curr_target)) in mem:
        #          return mem[key]


        #      minus_path = dfs(idx + 1, curr_target - nums[idx])
        #      add_path = dfs(idx + 1, curr_target + nums[idx])

        #      mem[key] = minus_path + add_path
        #      return mem[key]


        #  return dfs(0, target)
