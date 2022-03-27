# 845. Longest Mountain in Array
# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 1
        n = len(arr)
        res = 0
        while i < n:
            while i < n and arr[i - 1] == arr[i]:
                i += 1

            up = 0
            while i < n and arr[i - 1] < arr[i]:
                i += 1
                up += 1

            down = 0
            while i < n and arr[i - 1] > arr[i]:
                i += 1
                down += 1

            if up > 0 and down > 0:
                res = max(res, up + down + 1)

        return res