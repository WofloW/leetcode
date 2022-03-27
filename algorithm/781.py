# 781. Rabbits in Forest
# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        counter = collections.Counter(answers)
        for k, v in counter.items():
            ans += math.ceil(v / (k + 1)) * (k + 1)
        return ans