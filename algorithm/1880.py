# 1880. Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.word2int(firstWord) + self.word2int(secondWord) == self.word2int(targetWord)

    def word2int(self, word):
        return int(''.join([str(ord(c) - ord('a')) for c in word]))
