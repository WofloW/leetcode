# 816. Ambiguous Coordinates
# https://leetcode.com/problems/ambiguous-coordinates/

# String
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        def f(s):
            if not s or len(s) > 1 and s[0] == s[-1] == '0': return []
            if s[-1] == '0': return [s]
            if s[0] == '0': return ['0.' + s[1:]]
            return [s] + [f'{s[:i]}.{s[i:]}' for i in range(1, len(s))]

        return [f'({a}, {b})' for i in range(len(s)) for a, b in itertools.product(f(s[:i]), f(s[i:]))]