# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest

        # return max(accumulate(gain, initial=0))