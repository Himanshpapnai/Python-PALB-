class Solution:
    def vowelCount(self, s: str) -> int:
        import math
        from collections import Counter
        counts = Counter(s)
        freqs = [counts[v] for v in "aeiou" if counts[v] > 0]
        if not freqs: 
            return 0
        return math.prod(freqs) * math.factorial(len(freqs))
