class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        if n == 0:
            return 0
        low, high = 0, n - 1
        pivot = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < arr[0]:
                pivot = mid
                high = mid - 1
            else:
                low = mid + 1
        def binary_search_count(l, r):
            count = 0
            start, end = l, r
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] <= x:
                    count = mid - l + 1
                    start = mid + 1
                else:
                    end = mid - 1
            return count
        return binary_search_count(0, pivot - 1) + binary_search_count(pivot, n - 1)
        
