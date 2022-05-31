# 1812. Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        r = int(coordinates[1]) - 1
        c = ord(coordinates[0]) - ord('a')
        return r % 2 != c % 2
