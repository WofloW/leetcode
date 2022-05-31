# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/

# string manipulate
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        buckets = [''] * len(words)
        for word in words:
            buckets[int(word[-1]) - 1] = word[:-1]
        return ' '.join(buckets)

