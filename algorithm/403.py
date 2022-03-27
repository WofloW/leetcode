# 403. Frog Jump
# https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones == [0, 1]:
            return True
        stone_set = set(stones)
        stone_mem = defaultdict(set)
        stone_mem[1] = [1]
        for stone in stones[1:]:
            for k in stone_mem[stone]:
                for dx in [-1, 0, 1]:
                    if k + dx == 0:
                        continue
                    next_stone = stone + k + dx
                    if next_stone == stones[-1]:
                        return True
                    if next_stone in stone_set:
                        stone_mem[next_stone].add(k + dx)
        return False