# 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii/

from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set([start])
        n = len(arr)

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True

            for j in [i + arr[i], i - arr[i]]:
                if 0 <= j < n and j not in visited:
                    q.append(j)
                    visited.add(j)

        return False