# 1552. Magnetic Force Between Two Balls
# https://leetcode.com/problems/magnetic-force-between-two-balls/

# binary search
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        left, right = 1, (position[-1] - position[0]) // (m - 1) + 1

        def is_possible(gap):
            last_index = 0
            remaining_balls = m - 1
            for i in range(n):
                if position[i] - position[last_index] >= gap:
                    remaining_balls -= 1
                    last_index = i
                    if remaining_balls == 0:
                        break
            return remaining_balls == 0

        while left + 1 < right:
            mid = (left + right) // 2
            if is_possible(mid):
                left = mid
            else:
                right = mid
        if is_possible(right):
            return right
        return left
