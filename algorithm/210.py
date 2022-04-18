# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        graph = defaultdict(list)
        degrees = [0] * n
        for a, b in prerequisites:
            graph[b].append(a)
            degrees[a] += 1

        res = [i for i in range(n) if degrees[i] == 0]
        queue = deque(res)

        while queue:
            i = queue.popleft()
            for a in graph[i]:
                degrees[a] -= 1
                if degrees[a] == 0:
                    queue.append(a)
                    res.append(a)
        if len(res) != n:
            return []
        return res

