class Solution:
    def getMinMax(self, arr):
        arr_min=arr[0]
        arr_max=arr[0]
        for i in range(1,len(arr)):
            if(arr_min>arr[i]):
                arr_min=arr[i]
            if (arr_max<arr[i]):
                arr_max=arr[i]
        return(arr_min,arr_max)
