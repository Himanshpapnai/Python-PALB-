class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        
        def canPlace(min_diff):
            count = 1
            last_pos = arr[0]
            for i in range(1, n):
                if arr[i] - last_pos >= min_diff:
                    count += 1
                    last_pos = arr[i]
            return count >= k

        low = 0
        high = arr[-1] - arr[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return result
