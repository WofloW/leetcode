# 752. Open the Lock
# https://leetcode.com/problems/open-the-lock/

# two-way BFS
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = set(['0000'])
        end = set([target])
        visited = set(deadends)
        step = 0
        while start and end:
            if len(start) > len(end):
                start, end = end, start
            tmp = set()
            for wheel in start:
                if wheel in end:
                    return step
                if wheel in visited:
                    continue
                visited.add(wheel)
                for i in range(4):
                    s1 = self.tick(wheel, i, 1)
                    if s1 not in visited:
                        tmp.add(s1)
                    s2 = self.tick(wheel, i, -1)
                    if s2 not in visited:
                        tmp.add(s2)
            start = tmp
            step += 1
        return -1

    def tick(self, wheel, position, move):
        return wheel[:position] + str((int(wheel[position]) + move) % 10) + wheel[position + 1:]
