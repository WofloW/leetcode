# 2078. Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)
        for i in range(n):
            if colors[i] != colors[0]:
                res = max(res, i)
            if colors[i] != colors[-1]:
                res = max(res, n - 1 - i)
        return res