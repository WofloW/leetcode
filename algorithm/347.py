# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/


# Heap O(nlgn)
# bucket O(n)


# import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c = Counter(nums)
        # heap = []
        # for num, freq in c.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # while heap:
        #     res.append(heapq.heappop(heap)[1])
        # return reversed(res)

        buckets = [[] for _ in range(len(nums) + 1)]
        c = Counter(nums)
        for num, freq in c.items():
            buckets[freq].append(num)

        i = len(nums)
        res = []
        while len(res) < k:
            res += buckets[i]
            i -= 1
        # res = list(chain(*buckets))

        return res[:k]