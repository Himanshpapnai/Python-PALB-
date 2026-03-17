class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        arr.sort()
        ans = arr[n-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[n-1] - k
        
        for i in range(n - 1):
            min_h = min(smallest, arr[i+1] - k)
            max_h = max(largest, arr[i] + k)
            if min_h < 0:
                continue
            ans = min(ans, max_h - min_h)
            
        return ans
        
