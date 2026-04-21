class Solution:
    def substrWithVowels(self, s1, s2):
        from collections import defaultdict
        required_vowels = set(s1)
        target_count = len(required_vowels)
        window_counts = defaultdict(int)
        distinct_vowels_in_window = 0
        min_length = float('inf')
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            if char in required_vowels:
                if window_counts[char] == 0:
                    distinct_vowels_in_window += 1
                window_counts[char] += 1
            while distinct_vowels_in_window == target_count:
                min_length = min(min_length, right - left + 1)
                left_char = s2[left]
                if left_char in required_vowels:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] == 0:
                        distinct_vowels_in_window -= 1
                left += 1
        return int(min_length) if min_length != float('inf') else -1
