# 908. Smallest Range I
# https://leetcode.com/problems/smallest-range-i/


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # max_n = max(nums)
        # min_n = min(nums)
        # if max_n - k <= min_n + k:
        #     return 0
        # else:
        #     return max_n - k - min_n - k
        return max(0, max(nums) - 2 * k - min(nums))