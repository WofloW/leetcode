# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        mono_stack = [-1]

        res = 0
        for i, h in enumerate(heights):
            while h < heights[mono_stack[-1]]:
                left = mono_stack.pop()
                res = max(res, (i - mono_stack[-1] - 1) * heights[left])
            mono_stack.append(i)
        return res
