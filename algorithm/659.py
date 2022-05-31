# 659. Split Array into Consecutive Subsequences
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/


from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remaining = Counter(nums)
        ends_with = defaultdict(int)

        for num in nums:
            if remaining[num] == 0:
                continue
            remaining[num] -= 1
            if ends_with[num - 1] > 0:
                ends_with[num - 1] -= 1
                ends_with[num] += 1
            elif remaining[num + 1] > 0 and remaining[num + 2] > 0:
                remaining[num + 1] -= 1
                remaining[num + 2] -= 1
                ends_with[num + 2] += 1
            else:
                return False
        return True