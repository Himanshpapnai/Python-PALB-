class Solution:
    def countBalanced(self, arr):
        prefix_sums = {0: 1}
        
        current_sum = 0
        total_balanced = 0
        vowels = set("aeiou")
        for s in arr:
            string_score = 0
            for char in s:
                if char in vowels:
                    string_score += 1
                else:
                    string_score -= 1
            current_sum += string_score
            if current_sum in prefix_sums:
                total_balanced += prefix_sums[current_sum]
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
        return total_balanced
