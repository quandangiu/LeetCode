# 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        return [findFirst(nums, target), findLast(nums, target)]


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(sol.searchRange([], 0))  # [-1, -1]
