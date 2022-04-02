# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ''

    def is_palindrome(self, word):
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def is_palindrome2(self, word):
        return word == word[::-1]