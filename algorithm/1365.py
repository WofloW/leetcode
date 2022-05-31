# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# bucket
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num + 1] += 1
        for i in range(1, 102):
            count[i] += count[i - 1]
        return [count[num] for num in nums]
