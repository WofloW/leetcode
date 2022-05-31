# 650. 2 Keys Keyboard
# https://leetcode.com/problems/2-keys-keyboard/

# math
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans