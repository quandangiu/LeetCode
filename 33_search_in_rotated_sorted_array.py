# 33. Search in Rotated Sorted Array
# Difficulty: Medium
# Given an integer array nums sorted in ascending order (with distinct values) possibly rotated,
# and an integer target, return the index of target if it is in nums, or -1 if it is not.

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
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
