# 1944. Number of Visible People in a Queue
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] < v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res