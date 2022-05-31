# 1492. The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for x in range(1, int(n ** 0.5) + 1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
        for x in range(int(n ** 0.5), 0, -1):
            if x * x == n:
                continue
            if n % x == 0:
                k -= 1
                if k == 0:
                    return n // x
        return -1