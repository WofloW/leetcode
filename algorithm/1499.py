# 1499. Max Value of Equation
# https://leetcode.com/problems/max-value-of-equation/

#heap
# time O(nlogn)
# space O(n)
class Solution1:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = float('-inf')
        heap = []
        for x, y in points:
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                res = max(-heap[0][0] + y + x, res)
            heapq.heappush(heap, (x - y, x))
        return res


# monotonic queue
# time O(n)
# space O(n)
class Solution2:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = float('-inf')
        mono_q = collections.deque()
        for x, y in points:
            while mono_q and x - mono_q[0][1] > k:
                mono_q.popleft()
            if mono_q:
                res = max(res, mono_q[0][0] + x + y)
            while mono_q and mono_q[-1][0] < y - x:
                mono_q.pop()
            mono_q.append((y - x, x))
        return res