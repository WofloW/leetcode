# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [[0] * 3 for _ in range(2)]
        cols = [[0] * 3 for _ in range(2)]
        player = 0

        diags = [[0] * 2 for _ in range(2)]

        for r, c in moves:
            rows[player][r] += 1
            cols[player][c] += 1
            diags[player][0] += 1 if r == c else 0
            diags[player][1] += 1 if r + c == 2 else 0

            if rows[player][r] == 3 or cols[player][c] == 3 or diags[player][0] == 3 or diags[player][1] == 3:
                return 'AB'[player]
            player ^= 1

        return 'Draw' if len(moves) == 9 else 'Pending'