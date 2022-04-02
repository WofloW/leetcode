# 357. Count Numbers with Unique Digits
# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        ans = product = 1

        for i in range(n):
            product *= choices[i]
            ans += product

        return ans