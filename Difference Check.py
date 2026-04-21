class Solution:
    def minDifference(self, arr):
        def to_seconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s
        times = sorted([to_seconds(t) for t in arr])
        n = len(times)
        min_diff = (86400 - times[-1]) + times[0]
        for i in range(n - 1):
            diff = times[i+1] - times[i]
            if diff < min_diff:
                min_diff = diff
                
        return min_diff
