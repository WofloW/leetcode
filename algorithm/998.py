# 998. Maximum Binary Tree II
# https://leetcode.com/problems/maximum-binary-tree-ii/

# Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursion
        # if root and root.val > val:
        #     root.right = self.insertIntoMaxTree(root.right, val)
        #     return root
        # node = TreeNode(val)
        # node.left = root
        # return node

        # Iteration
        pre, cur = None, root
        while cur and cur.val > val:
            pre = cur
            cur = cur.right
        node = TreeNode(val)
        node.left = cur
        if pre:
            pre.right = node
        return root if root.val > val else node
