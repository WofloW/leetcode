# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Buy as many times as you want
# DP

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i0 = 0
        i1 = float('-inf')
        for price in prices:
            i0 = max(i0, i1 + price)
            i1 = max(i1, i0 - price)
        return i0