# 66. Plus One
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry != 1:
                break
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0
        if carry == 1:
            digits = [1] + digits
        return digits


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         index = len(digits) - 1
#         while digits[index] == 9:
#             digits[index] = 0
#             index -= 1
#
#         if index == -1:
#             digits = [1] + digits
#         else:
#             digits[index] += 1
#
#         return digits