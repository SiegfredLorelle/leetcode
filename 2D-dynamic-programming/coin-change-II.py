"""Coin Change II
You are given an integer array coins representing 
coins of different denominations and an 
integer amount representing a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return 0.

You may assume that you have an infinite number of each kind of coin.

The final answer is guaranteed to fit into a signed 32-bit integer.
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # # Bottom Up Approach
        # # Time: O(amount * len(coins))
        # # Space: O(amount)
        row = [0] * (amount + 1)
        row[-1] = 1

        for coin in coins:
            for curr_amount in range(amount - coin, -1, -1):
                new_amount = curr_amount + coin
                row[curr_amount] += row[new_amount]

        return row[0]




        # # Top Down Approach via memoization
        # # Time: O(amount * len(coins))
        # # Space: O(amount * len(coins))
        # mem = {}

        # def dfs(coin_idx, curr_amount):
        #     if coin_idx >= len(coins):
        #         return 0
        #     if curr_amount > amount:
        #         return 0
        #     if curr_amount == amount:
        #         return 1
        #     if (key := (coin_idx, curr_amount)) in mem:
        #         return mem[key]


        #     mem[key] = (
        #         dfs(coin_idx, curr_amount + coins[coin_idx])
        #         + dfs(coin_idx + 1, curr_amount)
        #     )

        #     return mem[key]



        # return dfs(0, 0)

