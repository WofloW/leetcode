# 2064. Minimized Maximum of Products Distributed to Any Store
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

# Binary search

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start, end = 1, max(quantities)
        while start < end:
            mid = (start + end) // 2
            if sum([math.ceil(q / mid) for q in quantities]) > n:
                start = mid + 1
            else:
                end = mid

        return start
