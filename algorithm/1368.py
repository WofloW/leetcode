# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution:
    def minCost(self, A):
        m, n, inf, k = len(A), len(A[0]), 10 ** 5, 0
        dp = [[inf] * n for _ in range(m)]
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = []

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n and dp[x][y] == inf):
                return
            dp[x][y] = k
            queue.append((x, y))
            dfs(x + DIR[A[x][y] - 1][0], y + DIR[A[x][y] - 1][1])

        dfs(0, 0)
        while queue:
            k += 1
            queue, queue2 = [], queue
            for x, y in queue2:
                for i, j in DIR:
                    dfs(x + i, y + j)
        return dp[-1][-1]