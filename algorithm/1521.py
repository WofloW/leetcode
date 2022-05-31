# 1521. Find a Value of a Mysterious Function Closest to Target
# https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        s = set()
        res = float('inf')
        for a in arr:
            s = {a & b for b in s} | {a}

            for k in s:
                res = min(res, abs(k - target))
        return res