"""Coin Change
You are given an integer array coins representing 
coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in mem.keys():
                return mem[amount]

            minimumCoinsUsed = float("infinity")
            for coin in coins:
                amountLeft = amount - coin
                if amountLeft < 0:
                    continue
                coinsUsed = dfs(amountLeft)
                minimumCoinsUsed = min(minimumCoinsUsed, 1 + coinsUsed)

            mem[amount] = minimumCoinsUsed
            return minimumCoinsUsed

        minimumCoinsUsed = dfs(amount)
        if minimumCoinsUsed == float("infinity"):
            return -1
        return minimumCoinsUsed
