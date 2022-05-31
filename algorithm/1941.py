# 1941. Check if All Characters Have Equal Number of Occurrences
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/


from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        prev = 0
        for v, count in counter.items():
            if prev == 0:
                prev = count
            else:
                if prev != count:
                    return False
        return True

class Solution1:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
