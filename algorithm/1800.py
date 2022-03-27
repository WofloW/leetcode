# 1800. Maximum Ascending Subarray Sum
# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        tmp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tmp += nums[i]
            else:
                tmp = nums[i]
            max_sum = max(max_sum, tmp)
        return max_sum