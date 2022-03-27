# 1504. Count Submatrices With All Ones
# https://leetcode.com/problems/count-submatrices-with-all-ones/

# fix the top left point 1
# find the possible submatrices below
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        arr = [[0] * n for _ in range(m)]

        for i in range(m):
            max_continous_one = 0
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    max_continous_one += 1
                else:
                    max_continous_one = 0
                arr[i][j] = max_continous_one

        ans = 0
        for i in range(m):
            for j in range(n):
                longest = sys.maxsize
                for new_i in range(i, m):
                    longest = min(longest, arr[new_i][j])
                    ans += longest
        return ans