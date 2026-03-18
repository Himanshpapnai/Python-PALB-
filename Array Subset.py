class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        counts = {}
        for x in a:
            counts[x] = counts.get(x, 0) + 1
        for x in b:
            if counts.get(x, 0) > 0:
                counts[x] -= 1
            else:
                return "No"
        return "Yes"
