# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        acc_costs = [0] * (n + 1)
        for i in range(2, n + 1):
            acc_costs[i] = min(acc_costs[i - 1] + cost[i - 1], acc_costs[i - 2] + cost[i - 2])
        return acc_costs[n]

