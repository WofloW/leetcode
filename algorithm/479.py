# 479. Largest Palindrome Product
# https://leetcode.com/problems/largest-palindrome-product/

class Solution:
    def largestPalindrome(self, n: int) -> int:
        high = 10 ** n - 1
        low = high // 10

        for large in range(high, low, -1):
            right = 0
            tmp = left = large
            while tmp != 0:
                right = right * 10 + tmp % 10
                tmp //= 10
                left *= 10
            pal = left + right

            for div in range(high, int(pal ** 0.5) - 1, -1):
                if pal // div > div:
                    break
                if pal % div == 0:
                    return pal % 1337
        return 9