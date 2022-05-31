# 1646. Get Maximum in Generated Array
# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            if i & 1 == 0:
                dp.append(dp[i // 2])
            else:
                dp.append(dp[i // 2] + dp[i // 2 + 1])
        return max(dp[:(n + 1)])
