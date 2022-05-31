# 2165. Smallest Value of the Rearranged Number
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

# int string
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        s = sorted(str(abs(num)))
        if num < 0:
            return -(int(''.join(s[::-1])))

        c = next(i for i, a in enumerate(s) if a > '0')
        s[0], s[c] = s[c], s[0]
        return int(''.join(s))