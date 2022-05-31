# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i, j = 0, len(row) - 1
            while i <= j:
                if row[i] == row[j]:
                    row[i] = row[j] = row[i] ^ 1
                i += 1
                j -= 1
        return image