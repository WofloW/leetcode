# 927. Three Equal Parts
# https://leetcode.com/problems/three-equal-parts/

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        indexes = [i for i in range(len(arr)) if arr[i] == 1]
        m = len(indexes)

        if m == 0:
            return [0, 2]

        if m % 3 != 0:
            return [-1, -1]

        part0_i = indexes[0]
        part1_i = indexes[m // 3]
        part2_i = indexes[m // 3 * 2]

        while part2_i < n:
            if arr[part0_i] == arr[part1_i] == arr[part2_i]:
                part0_i += 1
                part1_i += 1
                part2_i += 1
            else:
                return [-1, -1]
        else:
            return [part0_i - 1, part1_i]
