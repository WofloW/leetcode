# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/
# Segment tree

class Node:
    def __init__(self, i, j):
        self.start = i
        self.end = j
        self.total = None
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        def build_tree(nums, start, end):
            if start > end:
                return None

            if start == end:
                node = Node(start, end)
                node.total = nums[start]
                return node

            mid = (start + end) // 2

            node = Node(start, end)
            node.left = build_tree(nums, start, mid)
            node.right = build_tree(nums, mid + 1, end)
            node.total = node.left.total + node.right.total
            return node

        self.root = build_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def helper(root, i, val):
            if root.start == root.end == i:
                root.total = val
                return root

            mid = (root.start + root.end) // 2
            if i <= mid:
                helper(root.left, i, val)

            if i > mid:
                helper(root.right, i, val)

            root.total = root.left.total + root.right.total

        helper(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def helper(root, l, r):
            if root.start == l and root.end == r:
                return root.total

            mid = (root.start + root.end) // 2
            if l > mid:
                return helper(root.right, l, r)

            if r <= mid:
                return helper(root.left, l, r)

            return helper(root.left, l, mid) + helper(root.right, mid + 1, r)

        return helper(self.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)