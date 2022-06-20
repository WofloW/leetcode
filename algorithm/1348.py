# 1348. Tweet Counts Per Frequency
# https://leetcode.com/problems/tweet-counts-per-frequency/

# dict
class TweetCounts:

    def __init__(self):
        self.dict = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.dict.setdefault(tweetName, []).append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            seconds = 60
        elif freq == 'hour':
            seconds = 3600
        else:
            seconds = 86400

        res = [0] * ((endTime - startTime) // seconds + 1)
        for time in self.dict[tweetName]:
            if startTime <= time <= endTime:
                res[(time - startTime) // seconds] += 1
        return res