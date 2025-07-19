"""House Robber II
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and
it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money
you can rob tonight without alerting the police.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        mem = [ [-1, -1] for _ in range(len(nums)) ]

        def dfs(idx, allow_last):
            if idx >= len(nums):
                return 0
            if not allow_last and idx == len(nums) - 1:
                return 0
            if mem[idx][allow_last] != -1:
                return mem[idx][allow_last]

            rob_current = nums[idx] + dfs(idx + 2, allow_last)
            skip_current = dfs(idx + 1, allow_last)

            mem[idx][allow_last] = max(rob_current, skip_current)
            return mem[idx][allow_last]

        # rob first house, cannot rob last house
        case1 = dfs(0, 0)
        # skip first house, may rob last house
        case2 = dfs(1, 1)
        return max(case1, case2)
