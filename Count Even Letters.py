class Solution:
    def count(self, s):
        from collections import Counter
        frequencies = Counter(s)
        even_count = 0
        for char in frequencies:
            if frequencies[char] > 0 and frequencies[char] % 2 == 0:
                even_count += 1
                
        return even_count
