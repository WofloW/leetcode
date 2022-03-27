class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
      
'''
Algorithm:
Make use of the existing result
f(i) = f(i // 2) + i & 1

'''
