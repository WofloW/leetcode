# 855. Exam Room
# https://leetcode.com/problems/exam-room/

class ExamRoom:

    def __init__(self, n: int):
        self.N, self.occupied = n, []

    def seat(self) -> int:
        N, occupied = self.N, self.occupied

        res = 0
        position = 0
        if not occupied:
            res = 0
        else:
            d = occupied[0]
            for i in range(1, len(occupied)):
                a, b = occupied[i - 1], occupied[i]
                if (b - a) // 2 > d:
                    res = (a + b) // 2
                    d = (b - a) // 2
                    position = i

            if N - 1 - occupied[-1] > d:
                res = N - 1
                position = N - 1

        self.occupied.insert(position, res)
        return res

    def leave(self, p: int) -> None:
        self.occupied.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)