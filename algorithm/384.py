# 384. Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        ans = self.nums[:]
        for i in range(len(self.nums) - 1):
            j = random.randint(i, len(self.nums) - 1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()