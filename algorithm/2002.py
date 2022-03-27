# 2002. Maximum Product of the Length of Two Palindromic Subsequences
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        pairs = []
        for mask in range(1, 1 << n):
            string = ''
            for i in range(n):
                if mask & (1 << i) > 0:
                    string += s[i]
            if string == string[::-1]:
                pairs.append((mask, len(string)))

        m = len(pairs)
        res = 0
        for i in range(m):
            for j in range(i, m):
                if pairs[i][0] & pairs[j][0] == 0:
                    res = max(res, pairs[i][1] * pairs[j][1])
        return res
