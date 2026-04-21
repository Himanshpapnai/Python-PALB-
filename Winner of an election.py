class Solution:
    def winner(self, arr):
        from collections import Counter
        vote_counts = Counter(arr)
        winner_name = ""
        max_votes = -1
        for candidate, votes in vote_counts.items():
            if votes > max_votes:
                max_votes = votes
                winner_name = candidate
            elif votes == max_votes:
                if candidate < winner_name:
                    winner_name = candidate
        return [winner_name, str(max_votes)]
