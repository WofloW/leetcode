# 1163. Last Substring in Lexicographical Order
# https://leetcode.com/problems/last-substring-in-lexicographical-order/

# Hard
# baaa > ba
# bax > bac
# Two pointer
# s[i: i + l]   s[j: j + l]
# bea < bex
# so
# ea < ex
# a < x
# skip bea  i += l + 1
# s[i: i + l]    s[j: j + l]
# bex > bea
# so
# ex > ea
# x > a
# skip bea  j += l + 1

class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, l = 0, 1, 0
        n = len(s)
        while i + l < n and j + l < n:
            if s[i + l] == s[j + l]:
                l += 1
            else:
                if s[i + l] > s[j + l]:
                    j += l + 1
                else:
                    i += l + 1
                if i == j:
                    j += 1
                l = 0
        return s[i:]