"""
Best Time to Buy and Sell Stock

You are given an array prices 
where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by 
choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """ SOLUTION USING FOR LOOPS """
        max_profit = 0
        current_buy = prices[0]

        for price in prices[1:]:
            # Check if selling today has higher profit
            profit = price - current_buy
            if profit > max_profit:
                max_profit = profit

            # Check if there it is a better day to buy the stock
            elif price < current_buy:
                current_buy = price

        return max_profit

        """ SOLUTION USING TWO POINTERS """
        # b, s = 0, 1 # buy pointer, sell pointer
        # max_profit = 0

        # while s < len(prices):
        #     profit = prices[s] - prices[b]
        #     if profit > max_profit:
        #         max_profit = profit
        #     if prices[b] > prices[s]:
        #         b = s
        #     s += 1

        # return max_profit



sol = Solution()
result = sol.maxProfit([7,1,5,3,6,4])
print(result)