# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

# Math
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for v in columnTitle:
            res = 26 * res + (ord(v) - ord('A') + 1)
        return res