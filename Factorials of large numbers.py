class Solution:
    def factorial(self, n):
        res_val = 1
        for i in range(2, N + 1):
            res_val *= i
        ans = [int(digit) for digit in str(res_val)]
        
        return ans
