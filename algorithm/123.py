# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

import sys

def max_profit(prices):
    buy1 = buy2 = -sys.maxsize
    sell1 = sell2 = 0
    for price in prices:
        sell2 = max(sell2, buy2 + price)
        buy2 = max(buy2, sell1 - price)
        sell1 = max(sell1, buy1 + price)
        buy1 = max(buy1, -price)
        print(buy1, sell1, buy2, sell2)
    return sell2

