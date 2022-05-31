# 598. Range Addition II
# https://leetcode.com/problems/range-addition-ii/

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_w = min(map(lambda x: x[0], ops))
        min_h = min(map(lambda x: x[1], ops))
        return min_w * min_h

