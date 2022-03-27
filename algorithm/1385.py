# 1385. Find the Distance Value Between Two Arrays
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        rv = 0
        for val in arr1:
            i = bisect.bisect(arr2, val)
            if (i == 0 or arr2[i-1] < val - d) and (i == len(arr2) or arr2[i] > val + d):
                rv += 1
        return rv