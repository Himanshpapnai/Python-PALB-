class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        length = len(arr)
        for i in range(length - 2):
            left = i + 1
            right = length - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return True
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return False
        
