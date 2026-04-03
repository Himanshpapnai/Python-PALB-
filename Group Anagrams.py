class Solution(object):
    def groupAnagrams(self, strs):
        import collections
        anagram_map = collections.defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
        return list(anagram_map.values())
