# 179. Largest Number
# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'

        def comparator(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0

        return ''.join(sorted(map(str, nums), key=functools.cmp_to_key(comparator)))