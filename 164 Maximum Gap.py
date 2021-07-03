import math

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, nums):
        if not nums or len(nums) < 2 or min(nums) == max(nums):
            return 0

        min_nums, max_nums = min(nums), max(nums)

        size = math.ceil((max_nums - min_nums) / (len(nums) - 1))
        bucket = [[None, None] for _ in range((max_nums - min_nums) // size + 1)]

        for i in nums:
            b = bucket[(i - min_nums) // size]
            b[0] = i if b[0] is None else min(b[0], i)
            b[1] = i if b[1] is None else max(b[1], i)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))


'''
Algorithm:
Bucket sort
The minimum value of max gap is (max - min) / (N - 1)
Divide the space min to max into N - 1 bucket
Throw the N-2 into the N - 1 bucket
At least one bucket is empty
The max gap is not gap inside one bucket
The max gap is min of larger bucket - max of adjacent smaller bucket(skip the empty bucket)

Notice:
bucket_size = math.ceil((max-min)/(N-1))
bucket_num = (max_nums - min_nums) // size + 1
choose_bucket = (value - min_mums) // bucket_size
'''
