# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def max_side(total, cuts):
            max_len = 0
            cuts.sort()
            m = len(cuts)
            for i in range(1, m):
                max_len = max(max_len, cuts[i] - cuts[i - 1])
            max_len = max(max_len, total - cuts[-1], cuts[0])
            return max_len

        max_height = max_side(h, horizontalCuts)
        max_width = max_side(w, verticalCuts)

        return (max_height * max_width) % (10 ** 9 + 7)