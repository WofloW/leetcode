# 970. Powerful Integers
# https://leetcode.com/problems/powerful-integers/

# math
import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        result = set()
        x_bound = math.ceil(math.log(bound, x)) if x != 1 else 1
        y_bound = math.ceil(math.log(bound, y)) if y != 1 else 1
        for i in range(x_bound):
            for j in range(y_bound):
                tmp = x ** i + y ** j
                if tmp > bound:
                    break
                result.add(tmp)
        return list(result)

class Solution1:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a = {x ** i for i in range(20) if x ** i < bound}
        b = {y ** j for j in range(20) if y ** j < bound}
        return list({m + n for m in a for n in b if m + n <= bound})