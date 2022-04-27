# 1894. Find the Student that Will Replace the Chalk
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

# Mod
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, a in enumerate(chalk):
            if k < a:
                return i
            k -= a
        return 0

