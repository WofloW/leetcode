# 473. Matchsticks to Square
# https://leetcode.com/problems/matchsticks-to-square/

# DFS, greedy
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        # Greedy using the largest
        matchsticks.sort(reverse=True)
        if matchsticks[0] > total // 4:
            return False

        buckets = [total // 4] * 4

        def dfs(pos):
            if pos == len(matchsticks):
                return True

            length = matchsticks[pos]
            for i in range(4):
                if buckets[i] >= length:
                    buckets[i] -= length
                    if dfs(pos + 1):
                        return True
                    buckets[i] += length
            return False

        return dfs(0)

