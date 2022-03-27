# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = {}
        q = [(0, k)]
        for u, v, w in times:
            graph[u].append((v, w))

        while q:
            time, node = heapq.heappop(q)
            if node not in visited:
                visited[node] = time
                for neighbor, t in graph[node]:
                    heapq.heappush(q, (time + t, neighbor))

        return max(visited.values()) if len(visited) == n else -1

