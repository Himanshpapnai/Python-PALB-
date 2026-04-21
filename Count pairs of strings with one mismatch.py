class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        n = len(arr)
        if n == 0: return 0
        m = len(arr[0])
        total_pairs = 0
        full_string_counts = defaultdict(int)
        pattern_map = defaultdict(int)
        
        for s in arr:
            full_string_counts[s] += 1
            for i in range(m):
                pattern = s[:i] + '*' + s[i+1:]
                pattern_map[pattern] += 1
        for count in pattern_map.values():
            if count > 1:
                total_pairs += (count * (count - 1)) // 2
        for s, count in full_string_counts.items():
            if count > 1:
                identical_pairs = (count * (count - 1)) // 2
                total_pairs -= (m * identical_pairs)
                
        return total_pairs
