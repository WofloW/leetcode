# 1116. Print Zero Even Odd
# https://leetcode.com/problems/print-zero-even-odd/

# threading
from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.gates = [Semaphore(), Semaphore(), Semaphore()]
        self.gates[0].acquire()
        self.gates[1].acquire()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.ct += 1
            self.gates[self.ct % 2].release()

    def even(self, printNumber):
        for _ in range(self.n // 2):
            self.gates[0].acquire()
            printNumber(self.ct)
            self.gates[2].release()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            self.gates[1].acquire()
            printNumber(self.ct)
            self.gates[2].release()