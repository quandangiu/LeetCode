# 35. Search Insert Position
# Difficulty: Easy
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the index where it would be inserted.

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.searchInsert([1, 3, 5, 6], 5))  # 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # 4
    print(sol.searchInsert([1, 3, 5, 6], 0))  # 0
