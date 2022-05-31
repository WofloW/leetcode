# 1424. Diagonal Traverse II
# https://leetcode.com/problems/diagonal-traverse-ii/

# matrix diagonal traverse
# diagonal traverse
# 1. traverse all elements and put the element into buckets where the key is x + y or x - y
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        buckets = []

        for i, x in enumerate(nums):
            for j, y in enumerate(x):
                if len(buckets) <= i + j:
                    buckets.append([])
                buckets[i + j].append(y)
        return [a for row in buckets for a in reversed(row)]
