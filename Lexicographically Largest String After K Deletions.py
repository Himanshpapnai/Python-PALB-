class Solution:
    def maxSubseq(self, s, k):
        to_remove = k
        stack = []
        for char in s:
            while stack and to_remove > 0 and stack[-1] < char:
                stack.pop()
                to_remove -= 1
            stack.append(char)
        return "".join(stack[:len(s) - k])
