# 553. Optimal Division
# https://leetcode.com/problems/optimal-division/

# String
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        if len(nums) <= 2: return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))