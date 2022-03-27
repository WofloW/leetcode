# 457. Circular Array Loop
# https://leetcode.com/problems/circular-array-loop/

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue

            slow = fast = i

            direction = nums[i] > 0

            while nums[slow] != 0 or nums[fast] != 0:
                slow = self.next(slow, nums, direction)
                fast = self.next(self.next(fast, nums, direction), nums, direction)

                if slow == -1 or fast == -1:
                    break

                if slow == fast:
                    return True

            slow = i
            while slow != -1:
                nums[slow] = 0
                slow = self.next(slow, nums, direction)

        return False

    def next(self, i, nums, direction):
        n = len(nums)
        if i == -1 or (nums[i] > 0) != direction:
            return -1

        next_idx = (i + nums[i]) % n

        if nums[next_idx] == 0 or i == next_idx:
            return -1

        return next_idx