# 1353. Maximum Number of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        i = 0
        d = 0
        heap = []
        n = len(events)
        res = 0
        while i < n or heap:
            if not heap:
                d = events[i][0]
            while i < n and events[i][0] <= d:
                heapq.heappush(heap, events[i][1])
                i += 1

            heapq.heappop(heap)
            res += 1
            d += 1
            while heap and heap[0] < d:
                heapq.heappop(heap)
        return res

#         events.sort(reverse=True)
#         heap = []
#         res = 0
#         d = 0
#         while events or heap:
#             if not heap:
#                 d = events[-1][0]
#             while events and events[-1][0] <= d:
#                 heapq.heappush(heap, events.pop()[1])

#             heapq.heappop(heap)
#             res += 1
#             d += 1
#             while heap and heap[0] < d:
#                 heapq.heappop(heap)
#         return res