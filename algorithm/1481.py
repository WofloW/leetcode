# 1481. Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

# Sort
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        counter = sorted(counter.values(), reverse=True)
        while k > 0:
            k -= counter.pop()
        return len(counter) + (k < 0)