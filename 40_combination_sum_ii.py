# 40. Combination Sum II
# Difficulty: Medium
# Given a collection of candidate numbers and a target number, 
# find all unique combinations where the candidate numbers sum to target.
# Each number may only be used once in the combination.

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Early termination since array is sorted
                if candidates[i] > remaining:
                    break
                
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))  # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print(sol.combinationSum2([2, 5, 2, 1, 2], 5))  # [[1, 2, 2], [5]]
