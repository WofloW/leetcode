# 2016. Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_v = sys.maxsize
        res = 0
        for v in nums:
            min_v = min(min_v, v)
            res = max(v - min_v, res)

        return res if res > 0 else -1