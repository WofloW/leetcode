# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, res, [])
        return res

    def dfs(self, node, targetSum, res, path):
        if not node:
            return

        targetSum -= node.val
        path.append(node.val)
        if not node.left and not node.right:
            if targetSum == 0:
                res.append(list(path))
        else:
            self.dfs(node.left, targetSum, res, path)
            self.dfs(node.right, targetSum, res, path)
        path.pop()

    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]
