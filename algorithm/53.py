# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            dp[i + 1] = max(0, dp[i]) + num
        return max(dp[1:])