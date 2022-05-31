# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root
