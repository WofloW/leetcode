# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i/

# Binary tree
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True

        new_n = Node(start, end)
        node = self.root
        while node:
            if start >= node.end:
                if not node.right:
                    node.right = new_n
                    return True
                node = node.right
            elif end <= node.start:
                if not node.left:
                    node.left = new_n
                    return True
                node = node.left
            else:
                return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)