# 47. Permutations II
# Difficulty: Medium
# Given a collection of numbers that might contain duplicates, 
# return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()  # Sort to handle duplicates
        used = [False] * len(nums)
        
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                
                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False
        
        backtrack([])
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.permuteUnique([1, 1, 2]))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    print(sol.permuteUnique([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
