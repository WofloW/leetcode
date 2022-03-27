# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        count = 0
        for c in s:
            if c == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += 1
        return res