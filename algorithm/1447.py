# 1447. Simplified Fractions
# https://leetcode.com/problems/simplified-fractions/

# Math
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if self.gcd(j, i) == 1:
                    res.append(f'{i}/{j}')
        return res

    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x
