# 1035. Uncrossed Lines
# https://leetcode.com/problems/uncrossed-lines/

# DP, Longest common subsequence(LCS)
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        #         m = len(nums1)
        #         n = len(nums2)
        #         dp = [[0] * (n + 1) for _ in range(m + 1)]

        #         for i in range(1, m + 1):
        #             for j in range(1, n + 1):
        #                 dp[i][j] =  max(dp[i][j - 1], dp[i - 1][j])
        #                 if nums1[i - 1] == nums2[j - 1]:
        #                     dp[i][j] =  max(dp[i][j], dp[i - 1][j - 1] + 1)
        #         return dp[m][n]
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i % 2][j] = max(dp[i % 2][j - 1], dp[(i - 1) % 2][j])
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - 1] + 1)
        return dp[m % 2][n]