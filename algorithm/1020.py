# 1020. Number of Enclaves
# https://leetcode.com/problems/number-of-enclaves/

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            for dx, dy in DIRECTIONS:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        for i in range(m):
            for j in [0, n - 1]:
                dfs(i, j)

        for i in [0, m - 1]:
            for j in range(n):
                dfs(i, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res
