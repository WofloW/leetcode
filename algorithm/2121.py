# 2121. Intervals Between Identical Elements
# https://leetcode.com/problems/intervals-between-identical-elements/

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        m, res = defaultdict(list), [0] * len(arr)
        for i, v in enumerate(arr):
            m[v].append(i)

        for x, l in m.items():
            pre = [0] * (len(l) + 1)
            for i in range(len(l)):
                pre[i + 1] = pre[i] + l[i]
            for i, v in enumerate(l):
                res[v] = (v * i - pre[i]) + ((pre[len(l)] - pre[i]) - v * (len(l) - (i)))
        return res
