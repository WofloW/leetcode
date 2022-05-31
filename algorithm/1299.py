# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], cur_max = cur_max, max(cur_max, arr[i])
        return arr