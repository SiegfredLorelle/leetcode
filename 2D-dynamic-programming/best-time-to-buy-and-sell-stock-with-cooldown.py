"""Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is 
the price of a given stock on the ith day.

Find the maximum profit you can achieve. 
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with 
the following restrictions:

After you sell your stock, 
you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
"""

from type import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # Bottom Up - time: O(n) space: O(1)
    # buy -> sell -> hold -> buy
    prev_sell = 0
    prev_hold = 0
    prev_buy = 0

    for idx in range(len(prices) - 1, -1, -1):
        # selling only happens after buying
        curr_sell = prev_buy
        # holding happens after selling
        curr_hold = max(prev_hold, prices[idx] + prev_sell)
        # buying happens after holding
        curr_buy = max(prev_buy, -prices[idx] + prev_hold)

        prev_sell = curr_sell
        prev_hold = curr_hold
        prev_buy = curr_buy

    return prev_buy



    # Top Down - time: O(n) space: O(n)
    # memo = {}

    # def dfs(i, is_buying):
    #     if i >= len(prices):
    #         return 0

    #     if (key := (i, is_buying)) in memo:
    #         return memo[key]

    #     cd = dfs(i + 1, is_buying)
    #     if is_buying:
    #         buy = dfs(i + 1, not is_buying) - prices[i]
    #         memo[key] = max(buy, cd)
    #     else:
    #         sell = dfs(i + 2, not is_buying) + prices[i]
    #         memo[key] = max(sell, cd)

    #     return memo[key]


    # return dfs(0, True)

