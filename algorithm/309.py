# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/share-my-thinking-process

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i0 = 0
        i0_pre = 0
        i1 = float('-inf')
        for price in prices:
            i0_old = i0
            i0 = max(i0, i1 + price)
            i1 = max(i1, i0_pre - price)
            i0_pre = i0_old
        return i0