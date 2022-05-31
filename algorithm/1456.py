# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# sliding window, set

VOWELS = {'a', 'e', 'i', 'o', 'u'}

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur = res = 0

        for i in range(len(s)):
            if s[i] in VOWELS:
                cur += 1

            if i >= k and s[i - k] in VOWELS:
                cur -= 1

            res = max(res, cur)

        return res
