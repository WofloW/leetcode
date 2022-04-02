# 2180. Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        digit_sum = 0
        tmp = num
        while tmp != 0:
            digit_sum += tmp % 10
            tmp //= 10

        return (num - (digit_sum & 1)) // 2