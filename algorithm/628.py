# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/

# Math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

        large3 = heapq.nlargest(3, nums)
        small2 = heapq.nsmallest(2, nums)
        return max(large3[0] * large3[1] * large3[2], small2[0] * small2[1] * large3[0])