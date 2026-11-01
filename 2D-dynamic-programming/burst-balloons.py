"""Burst Balloons

You are given n balloons, indexed from 0 to n - 1. 
Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.

If you burst the ith balloon, 
you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, 
then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
"""


class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        new_nums = [1] + nums + [1]
        mem = {}

        def dfs(left, right):
            if left > right:
                return 0

            key = (left, right)
            if key in mem:
                return mem[key]

            max_coins = 0
            for idx in range(left, right + 1):
                coins = new_nums[left - 1] * new_nums[idx] * new_nums[right + 1]
                coins += dfs(left, idx - 1) + dfs(idx + 1, right)

                max_coins = max(coins, max_coins)

            mem[key] = max_coins
            return max_coins


        return dfs(1, len(nums))
