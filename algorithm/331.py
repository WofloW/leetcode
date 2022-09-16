# 331. Verify Preorder Serialization of a Binary Tree
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        p_list = preorder.split(',')
        slot = 1
        for p in p_list:
            if slot == 0:
                return False

            if p == '#':
                slot -= 1
            else:
                slot += 1
        return slot == 0