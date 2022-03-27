# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/

# DFS
class Solution0:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return False
# BFS


class Solution1:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = collections.deque([source])
        visited = set()

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for edge in graph[node]:
                if edge not in visited:
                    q.append(edge)
                    visited.add(edge)
        return False



# union find
class Solution2:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find_parent(v):
            return v if v == parent[v] else find_parent(parent[v])

        parent = [i for i in range(n)]
        for edge in edges:
            pu = find_parent(edge[0])
            pv = find_parent(edge[1])
            parent[pu] = pv

        return find_parent(source) == find_parent(destination)
