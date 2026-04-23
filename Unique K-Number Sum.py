class Solution:
    def combinationSum(self, n, k):
        result = []
        
        def backtrack(start, current_combination, current_sum):
            if len(current_combination) == k:
                if current_sum == n:
                    result.append(list(current_combination))
                return
            for i in range(start, 10):
                if current_sum + i > n:
                    break
                current_combination.append(i)
                backtrack(i + 1, current_combination, current_sum + i)
                current_combination.pop()
        
        backtrack(1, [], 0)
        return result
