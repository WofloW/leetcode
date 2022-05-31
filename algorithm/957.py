# 957. Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        memo = {str(cells): n}
        while n:
            new_arr = [0] * 8
            for i in range(1, 7):
                new_arr[i] = 1 if not (cells[i - 1] ^ cells[i + 1]) else 0
            cells = new_arr
            n -= 1
            if str(cells) in memo:
                n %= memo[str(cells)] - n
            else:
                memo[str(cells)] = n
        return cells
