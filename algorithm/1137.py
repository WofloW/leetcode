# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution0:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c


class Solution1:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]

        for i in range(n - 2):
            dp[i % 3] = sum(dp)
        return dp[n % 3]