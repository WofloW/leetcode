# 2070. Most Beautiful Item for Each Query
# https://leetcode.com/problems/most-beautiful-item-for-each-query/

import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items + [[0, 0]])
        for i in range(len(items) - 1):
            items[i + 1][1] = max(items[i][1], items[i + 1][1])
        return [items[bisect.bisect(items, [q + 1]) - 1][1] for q in queries]