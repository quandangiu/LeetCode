class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result
