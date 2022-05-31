# 2144. Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum([price for i, price in enumerate(sorted(cost)) if (len(cost) - i) % 3 != 0])
