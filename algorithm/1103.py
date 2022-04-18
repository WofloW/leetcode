# 1103. Distribute Candies to People
# https://leetcode.com/problems/distribute-candies-to-people/

# The candies distributed on round 1
# (1 + n) * n // 2
# The candies distributed on round 2
# (1 + n) * n // 2 + n * n
#
# Calculate full round number k.
# In the full round:
# The 1st person gets the total candies 1, 1 + n, 1 + 2n, 1 + k * n
# (1 + (1 + k * n)) * k // 2
#
# The ith(1 indexed) person gets the total candies i, i + n, i + 2n, i + k * n
# (i + (i + k * n)) * k // 2
#
# Simulate the last round.
#
# Use sum of arithmetic sequence to save some time.

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        round = 0
        n = num_people
        last_round_sum = (1 + n) * n // 2
        # Calculate round num
        while candies - last_round_sum > 0:
            candies -= last_round_sum
            last_round_sum += n * n
            round += 1

        res = [0] * n
        for i in range(1, n + 1):
            # Calculate the total candies distributed in full round for each person
            res[i - 1] = (i + i + (round - 1) * n) * round // 2

            # Simulate last round
            if candies - (i + n * round) > 0:
                res[i - 1] += i + n * round
                candies -= i + n * round
            else:
                res[i - 1] += candies
                candies = 0
        return res




# Brute force
class Solution1:
    def distributeCandies(self, candies, n):
        res = [0] * n
        i = 0
        while candies > 0:
            res[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res


