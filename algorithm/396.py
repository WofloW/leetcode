# 396. Rotate Function
# https://leetcode.com/problems/rotate-function/

# Math
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        res = cur = sum(i * j for i, j in enumerate(nums))

        s = sum(nums)
        for i in range(1, n):
            cur = cur + s - n * nums[-i]
            res = max(res, cur)
        return res