# 1317. Convert Integer to the Sum of Two No-Zero Integers
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        while '0' in f'{a}{n - a}':
            a += 1
        return [a, n - a]
