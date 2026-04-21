class Solution:
    def search(self, txt: str, pat: str) -> bool:
        from collections import Counter
        n, m = len(txt), len(pat)
        if m > n:
            return False
        pat_counts = Counter(pat)
        window_counts = Counter(txt[:m])
        if pat_counts == window_counts:
            return True
        for i in range(m, n):
            window_counts[txt[i]] += 1
            left_char = txt[i - m]
            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                del window_counts[left_char]
            if pat_counts == window_counts:
                return True
        return False
