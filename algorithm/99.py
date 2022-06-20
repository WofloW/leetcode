# 99. Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/

# Binary search tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive with first and second
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None

        self.inorder(root)

        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if self.prev and node.val <= self.prev.val:
            if not self.first:
                self.first = self.prev
            self.second = node
        self.prev = node

        self.inorder(node.right)

# Recursive with list of wrong nodes. Note that the wrong nodes maybe len 1
class Solution1:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.wrong_nodes = []
        self.inorder(root)

        tmp = self.wrong_nodes[0][0].val
        self.wrong_nodes[0][0].val = self.wrong_nodes[-1][1].val
        self.wrong_nodes[-1][1].val = tmp

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if self.prev and node.val <= self.prev.val:
            self.wrong_nodes.append((self.prev, node))
        self.prev = node

        self.inorder(node.right)

# Iterative inorder
class Solution2:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        first = None
        second = None

        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()

            if prev and node.val <= prev.val:
                if not first:
                    first = prev
                second = node

            prev = node

            if node.right:
                cur = node.right

        tmp = first.val
        first.val = second.val
        second.val = tmp