# 139. Word Break
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * (len(s) + 1)
        d[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[i - len(word): i] == word and d[i - len(word)]:
                    d[i] = True
                    break
        return d[-1]
