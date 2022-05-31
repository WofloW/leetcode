# 1775. Equal Sum Arrays With Minimum Number of Operations
# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

# sort
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2) * 6 or len(nums1) * 6 < len(nums2):
            return -1
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:
            return self.minOperations(nums2, nums1)

        diff = sum2 - sum1
        nums1.sort()
        nums2.sort()

        i, j = 0, len(nums2) - 1
        res = 0
        while diff > 0:
            if j < 0 or i < len(nums1) and 6 - nums1[i] > nums2[j] - 1:
                diff -= 6 - nums1[i]
                i += 1
            else:
                diff -= nums2[j] - 1
                j -= 1
            res += 1
        return res

    def minOperations2(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
            return -1
        sm1, sm2 = map(sum, (nums1, nums2))
        if sm1 > sm2:
            return self.minOperations(nums2, nums1)
        cnt = Counter([6 - n for n in nums1] + [n - 1 for n in nums2])
        i, operations = 5, 0
        while sm2 > sm1:
            while cnt[i] == 0:
                i -= 1
            sm1 += i
            cnt[i] -= 1
            operations += 1
        return operations