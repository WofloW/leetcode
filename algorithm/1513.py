# 1513. Number of Substrings With Only 1s
# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        s1 = s.split('0')
        res = 0
        for sub in s1:
            n = len(sub)
            res += (1 + n) * n // 2
        return res % (10 ** 9 + 7)