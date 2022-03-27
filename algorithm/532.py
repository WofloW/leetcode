# 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0

        for i in counter:
            if (k != 0 and i + k in counter) or (k == 0 and counter[i] > 1):
                result += 1

        return result