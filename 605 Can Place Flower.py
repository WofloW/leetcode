class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, x in enumerate(flowerbed):
            if not x and (i == 0 or flowerbed[i - 1] == 0) \
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
            if n <= 0:
                return True 
        return False


'''
Algorithm:
Greedy
If I can place flower, then place and check next.

Notice:
Speed up the loop. When n <= 0 break.
'''