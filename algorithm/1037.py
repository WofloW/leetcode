# 1037. Valid Boomerang
# https://leetcode.com/problems/valid-boomerang/

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = points[0]
        b = points[1]
        c = points[2]
        return (a[0] - b[0]) * (a[1] - c[1]) != (a[0] - c[0]) * (a[1] - b[1])

