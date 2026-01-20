# 46. Permutations
# Difficulty: Medium
# Given an array nums of distinct integers, return all possible permutations. 
# You can return the answer in any order.

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(current, remaining):
            if not remaining:
                result.append(current[:])
                return
            
            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i + 1:])
                current.pop()
        
        backtrack([], nums)
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.permute([1, 2, 3]))
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    print(sol.permute([0, 1]))  # [[0, 1], [1, 0]]
    print(sol.permute([1]))  # [[1]]
