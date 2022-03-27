# 720. Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ''
        prefixs = set(words)
        res = 0
        options = []
        for word in words:
            for i in range(1, len(word)):
                if word[:i] not in prefixs:
                    break
            else:
                if len(word) > res:
                    res = len(word)
                    options = [word]
                if len(word) == res:
                    options.append(word)
        options.sort()
        if options:
            return options[0]
        else:
            return ''