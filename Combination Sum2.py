class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(remain, path, start):
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i + 1)
                path.pop()

        backtrack(target, [], 0)
        return res
        
