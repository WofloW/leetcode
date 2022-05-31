# 1030. Matrix Cells in Distance Order
# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = [(x, y) for x in range(rows) for y in range(cols)]
        return sorted(res, key=lambda p: abs(p[0] - rCenter) + abs(p[1] - cCenter))


from collections import deque

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


class Solution1:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        q = deque([[rCenter, cCenter]])
        res = []
        visited = {(rCenter, cCenter)}
        while q:

            point = q.popleft()
            res.append(point)

            x = point[0]
            y = point[1]
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                    q.append([new_x, new_y])
                    visited.add((new_x, new_y))
        return res




