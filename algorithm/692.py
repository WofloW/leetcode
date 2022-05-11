# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

# heap
from collections import Counter
import heapq


class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        else:
            return self.word > other.word

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, count in counter.items():
            heapq.heappush(heap, Node(count, word))
            if len(heap) > k:
                heapq.heappop(heap)
        # heap.sort(key=lambda x: (-x.count, x.word))
        # return map(lambda x: x.word, heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]