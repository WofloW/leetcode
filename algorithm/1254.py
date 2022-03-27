# 1254. Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/

DIR = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue

                if grid[i][j] == 1:
                    visited.add((i, j))
                    continue

                stack = [(i, j)]
                is_closed = True
                while stack:
                    x, y = stack.pop()
                    visited.add((x, y))
                    for dx, dy in DIR:
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            is_closed = False
                        elif (nx, ny) not in visited and grid[nx][ny] == 0:
                            stack.append((nx, ny))
                if is_closed:
                    res += 1
        return res

# paint color
class Solution1(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j, val):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = val
                dfs(i, j + 1, val)
                dfs(i + 1, j, val)
                dfs(i - 1, j, val)
                dfs(i, j - 1, val)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j, 1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1

        return res

# global variable
class Solution2:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(x, y):
            if x in (0, m - 1) or y in (0, n - 1):
                self.isIsland = False
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    grid[i][j] = -1
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.isIsland = True
                    dfs(i, j)
                    res += self.isIsland

        return res