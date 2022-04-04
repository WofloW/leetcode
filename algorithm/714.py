# 714. Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Greedy
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        minimum = prices[0]
        res = 0
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > fee:
                res += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return res
