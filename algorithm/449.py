# 449. Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/

# DFS, BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = []

        def preorder(root):
            if root:
                vals.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(left, right):
            if vals and left < vals[0] < right:
                v = vals.popleft()
                node = TreeNode(v)
                node.left = build(left, v)
                node.right = build(v, right)
                return node

        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans