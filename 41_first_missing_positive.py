# 41. First Missing Positive
# Difficulty: Hard
# Given an unsorted integer array nums, return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Place each number in its correct position
        # Number i should be at index i-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Find the first position where the number is not correct
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.firstMissingPositive([1, 2, 0]))  # 3
    print(sol.firstMissingPositive([3, 4, -1, 1]))  # 2
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))  # 1
