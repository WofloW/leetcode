# 1769. Minimum Number of Operations to Move All Balls to Each Box
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_count = left_cost = right_count = right_cost = 0
        n = len(boxes)
        res = [0] * n

        for i in range(1, n):
            if boxes[i - 1] == '1':
                left_count += 1
            left_cost += left_count
            res[i] = left_cost

        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                right_count += 1
            right_cost += right_count
            res[i] += right_cost
        return res