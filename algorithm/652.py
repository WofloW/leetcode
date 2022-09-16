# 652. Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        nodes = defaultdict(list)

        def preorder(node):
            if not node:
                return 'None'
            string = f'{node.val} {preorder(node.left)} {preorder(node.right)}'
            nodes[string].append(node)
            return string

        preorder(root)

        return [nodes[string][0] for string in nodes if len(nodes[string]) > 1]
