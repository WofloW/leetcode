class Solution:
    """
    @param n: a integer
    @param logs: a list of integers
    @return: return a list of integers
    """

    def read_log(self, log):
        splitted_log = log.split(':')
        function_id = int(splitted_log[0])
        start_end = splitted_log[1]
        time = int(splitted_log[2])
        return [function_id, start_end, time]

    def exclusiveTime(self, n, logs):
        # write your code here
        stack = []
        times = {}

        logs = list(map(self.read_log, logs))

        for i, log in enumerate(logs):
            function_id = log[0]
            start_end = log[1]
            time = log[2]
            if start_end == 'start':
                if stack:
                    key = stack[-1]
                    last_time = 0
                    if i >= 1:
                        last_time = logs[i - 1][2] + 1 if logs[i - 1][1] == 'end' else logs[i - 1][2]
                    times[key] = times.get(key, 0) + time - last_time
                stack.append(function_id)

            if start_end == 'end':
                key = stack[-1]

                times[key] = times.get(key, 0) + time - logs[i - 1][2] + (0 if logs[i - 1][1] == 'end' else 1)
                stack.pop()
        ans = []
        for i in range(0, n):
            ans.append(times[i])
        return ans


print(Solution().exclusiveTime(10, ["0:start:0", "1:start:4", "2:start:6", "3:start:11", "4:start:14", "5:start:17",
                                    "6:start:22", "7:start:25", "8:start:27", "9:start:31", "8:start:38", "8:end:43",
                                    "9:start:44", "9:end:49", "9:end:52", "8:end:54", "7:end:55", "6:end:60",
                                    "5:end:65", "0:start:68", "0:end:72", "4:end:75", "3:end:77", "2:end:81",
                                    "1:end:85", "0:end:88"]
                               ))
