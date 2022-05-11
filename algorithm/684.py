# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/

# Union Find with rank
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = [x for x in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py: return True
            if rank[px] > rank[py]:
                p[py] = px
                rank[x] += 1
            else:
                p[px] = py
                rank[y] += 1
            return False

        for edge in edges:
            if union(edge[0], edge[1]): return edge


# Union Find without rank
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [x for x in range(len(edges) + 1)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py: return True
            p[px] = py
            return False

        for edge in edges:
            if union(edge[0], edge[1]): return edge


# Graph DFS
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.already_connected = defaultdict(list)
        for edge in edges:
            self.visited = defaultdict(bool)
            x, y = edge[0], edge[1]
            if self.is_already_connected(x, y):
                return edge
            self.already_connected[x].append(y)
            self.already_connected[y].append(x)

    def is_already_connected(self, x, y):
        if x == y:
            return True
        for x_adjacent in self.already_connected[x]:
            if not self.visited[x_adjacent]:
                self.visited[x_adjacent] = True
                if self.is_already_connected(x_adjacent, y):
                    return True
        return False
