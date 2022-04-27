# 926. Flip String to Monotone Increasing
# https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = min_flips = s.count('0')
        for c in s:
            if c == '0':
                flips -= 1
            else:
                flips += 1
            min_flips = min(min_flips, flips)
        return min_flips