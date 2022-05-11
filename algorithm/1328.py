# 1328. Break a Palindrome
# https://leetcode.com/problems/break-a-palindrome/

# array iteration
class Solution:
    def breakPalindrome(self, S):
        for i in range(len(S) // 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        return S[:-1] + 'b' if len(S) != 1 else ''