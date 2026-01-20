# 39. Combination Sum
# Difficulty: Medium
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target.

class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
    print(sol.combinationSum([2, 3, 5], 8))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(sol.combinationSum([2], 1))  # []
