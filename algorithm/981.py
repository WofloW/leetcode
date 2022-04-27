# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/

# Binary search
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        array = self.store[key]
        left = 0
        right = len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid][0] < timestamp:
                left = mid
            elif array[mid][0] == timestamp:
                return array[mid][1]
            else:
                right = mid
        if array[right][0] <= timestamp:
            return array[right][1]
        if array[left][0] <= timestamp:
            return array[left][1]
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)