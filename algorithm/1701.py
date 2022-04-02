# 1701. Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total = 0
        for arrival, time in customers:
            current_time = max(current_time, arrival) + time
            total += current_time - arrival

        return total / len(customers)