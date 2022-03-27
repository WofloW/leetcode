# 2053. Kth Distinct String in an Array
# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)

        distinct = [c for c in arr if counter[c] == 1]

        return distinct[k - 1] if k <= len(distinct) else ''

