# 1329. Sort the Matrix Diagonally
# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        d = collections.defaultdict(list)

        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])

        for r in d:
            d[r].sort(reverse=True)

        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat