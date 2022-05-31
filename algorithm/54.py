# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []

        r_start = 0
        r_end = len(matrix) - 1

        c_start = 0
        c_end = len(matrix[0]) - 1

        while r_start <= r_end and c_start <= c_end:
            for j in range(c_start, c_end + 1):
                res.append(matrix[r_start][j])
            r_start += 1

            for i in range(r_start, r_end + 1):
                res.append(matrix[i][c_end])
            c_end -= 1

            if r_start <= r_end:
                for j in range(c_end, c_start - 1, -1):
                    res.append(matrix[r_end][j])
                r_end -= 1

            if c_start <= c_end:
                for i in range(r_end, r_start - 1, -1):
                    res.append(matrix[i][c_start])
                c_start += 1

        return res
