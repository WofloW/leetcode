# 1347. Minimum Number of Steps to Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

# counter
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ct = Counter(t)
        res = 0
        for c, v in cs.items():
            if c in ct:
                res += max(0, v - ct[c])
            else:
                res += v
        return res

    # def minSteps(self, s, t):
    #     charArray = [0] * 26
    #
    #     for char in s:
    #         charArray[ord(char) - ord('a')] += 1
    #
    #     for char in t:
    #         charArray[ord(char) - ord('a')] -= 1
    #
    #     count = 0
    #     for val in charArray:
    #         if val > 0:
    #             count += val
    #
    #     return count