# 1631. Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/

from heapq import heappop, heappush

DIR = [0, 1, 0, -1, 0]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[sys.maxsize] * n for _ in range(m)]

        min_heap = [(0, 0, 0)]

        while min_heap:
            d, r, c = heappop(min_heap)
            if d > dist[r][c]: continue
            if r == m - 1 and c == n - 1:
                return d
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    new_dist = max(abs(heights[nr][nc] - heights[r][c]), d)
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        heappush(min_heap, (new_dist, nr, nc))