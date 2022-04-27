# 1524. Number of Sub-arrays With Odd Sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = even = res = 0
        for v in arr:
            if v % 2:
                odd, even = even + 1, odd
            else:
                even += 1
            res = (res + odd) % (10 ** 9 + 7)
        return res

