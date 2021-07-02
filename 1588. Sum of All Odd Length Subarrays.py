class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        accumulated = 0
        accumulated_array = [0]
        for i in range(len(arr)):
            accumulated += arr[i]
            accumulated_array.append(accumulated)
            
        result = []
        
        for i in range(len(arr)):
            length = 1
            while i + length <= len(arr):
                result.append(accumulated_array[i + length] - accumulated_array[i])
                length += 2
                
        return sum(result)
        
'''
Algorithm:
Iterative
Find all start index with odd length
Use accumulated array

Notice:
Accumulated array starts with 0
The length of accumulated array is n + 1
'''
