# 900. RLE Iterator
# https://leetcode.com/problems/rle-iterator/

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.index = 0
        self.A = encoding

    def next(self, n: int) -> int:
        while self.index < len(self.A):
            if n <= self.A[self.index]:
                self.A[self.index] -= n
                return self.A[self.index + 1]
            n -= self.A[self.index]
            self.index += 2
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)