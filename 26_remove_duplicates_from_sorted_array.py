# 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
# such that each unique element appears only once. The relative order of the elements should be kept the same.

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k


# Test
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"k = {k1}, nums = {nums1[:k1]}")  # k = 2, nums = [1, 2]
    
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"k = {k2}, nums = {nums2[:k2]}")  # k = 5, nums = [0, 1, 2, 3, 4]
