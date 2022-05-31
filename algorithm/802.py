# 802. Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/

# topological sort

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        in_nodes = collections.defaultdict(list)
        indegrees = [0] * n
        for i,v in enumerate(graph):
            indegrees[i] = len(v)
            for e in v:
                in_nodes[e].append(i)
        q = [i for i in range(n) if indegrees[i] == 0]
        while q:
            x = q.pop()
            for e in in_nodes[x]:
                indegrees[e] -= 1
                if indegrees[e] == 0:
                    q.append(e)
        ans = [i for i in range(n) if indegrees[i]==0]
        return ans