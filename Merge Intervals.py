class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_interval_end = merged[-1][1]
            if current_start <= last_interval_end:
                merged[-1][1] = max(last_interval_end,current_end)
            else:
                merged.append(intervals[i])
                
        return merged
