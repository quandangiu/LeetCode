# 33. Search in Rotated Sorted Array
# Difficulty: Medium
# Given an integer array nums sorted in ascending order (with distinct values) possibly rotated,
# and an integer target, return the index of target if it is in nums, or -1 if it is not.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(sol.search([1], 0))  # -1
