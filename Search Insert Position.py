class Solution:
    def searchInsert(self, nums, target):

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(sol.searchInsert(nums1, target1))  
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(sol.searchInsert(nums2, target2))  
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(sol.searchInsert(nums3, target3))  
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(sol.searchInsert(nums4, target4)) 
        
