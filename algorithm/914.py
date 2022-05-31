# 914. X of a Kind in a Deck of Cards
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

# math
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        # def gcd(a, b):
        #     while b:
        #         a, b = b, a % b
        #     return a

        return reduce(math.gcd, c.values()) >= 2