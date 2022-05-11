# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

# Greedy
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        first_sum = sum(nums[0: k])
        second_sum = sum(nums[k: k * 2])
        third_sum = sum(nums[k * 2: k * 3])

        best_one_sum = first_sum
        best_two_sum = first_sum + second_sum
        best_three_sum = best_two_sum + third_sum

        best_one_index = [0]
        best_two_index = [0, k]
        best_three_index = [0, k, k * 2]

        first_pointer = 1
        second_pointer = k + 1
        third_pointer = k * 2 + 1

        while third_pointer <= n - k:
            first_sum += -nums[first_pointer - 1] + nums[first_pointer + k - 1]
            second_sum += -nums[second_pointer - 1] + nums[second_pointer + k - 1]
            third_sum += -nums[third_pointer - 1] + nums[third_pointer + k - 1]

            if first_sum > best_one_sum:
                best_one_sum = first_sum
                best_one_index = [first_pointer]

            if best_one_sum + second_sum > best_two_sum:
                best_two_sum = best_one_sum + second_sum
                best_two_index = best_one_index + [second_pointer]

            if best_two_sum + third_sum > best_three_sum:
                best_three_sum = best_two_sum + third_sum
                best_three_index = best_two_index + [third_pointer]

            first_pointer += 1
            second_pointer += 1
            third_pointer += 1
        return best_three_index
