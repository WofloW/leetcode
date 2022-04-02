# 1855. Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

# Iterate on nums2
class Solution1:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = res = 0
        for j, b in enumerate(nums2):
            while i < len(nums1) and nums1[i] > b:
                i += 1
            if i == len(nums1): break
            res = max(res, j - i)
        return res

# Iterate on nums1
class Solution2:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j, res = -1, 0
        for i, a in enumerate(nums1):
            while j + 1 < len(nums2) and a <= nums2[j + 1]:
                j += 1
            res = max(res, j - i)
        return res


# Iterate on nums1 and nums2
class Solution3:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res
