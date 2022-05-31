# 486. Predict the Winner
# https://leetcode.com/problems/predict-the-winner/


# dp
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = list(nums)
        n = len(nums)

        if n & 1 == 0:
            return True

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])

        return dp[0] >= 0

#         n = len(nums)
#         dp = [[0] * n for _ in range(n)]

#         for i in range(n):
#             dp[i][i] = nums[i]

#         for l in range(2, n + 1):
#             for i in range(n - l + 1):
#                 j = i + l - 1
#                 dp[i][j] = max(nums[i] - dp[i + 1][j],
#                               nums[j] - dp[i][j - 1])

#         return dp[0][n - 1] >= 0