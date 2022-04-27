# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

# sort

# Counter().most_common()
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        res = [k * v for k, v in Counter(s).most_common()]
        return ''.join(res)

# sort the counter and rebuild the result
from collections import Counter
class Solution1:
    def frequencySort(self, s: str) -> str:
        counter = [(v, k) for k, v in Counter(s).items()]
        counter.sort(reverse=True)
        res = []
        for freq, char in counter:
            res.append(char * freq)
        return ''.join(res)

# sort all string based on frequency
from collections import Counter
class Solution2:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        s = list(s)
        s.sort(key=lambda x: (-counter[x], x))
        return ''.join(s)