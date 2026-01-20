# 27. Remove Element
# Difficulty: Easy
# Given an integer array nums and an integer val, remove all occurrences of val in-place.
# The order of the elements may be changed. Return the number of elements not equal to val.

class Solution:
    def removeElement(self, nums, val):
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


# Test
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [3, 2, 2, 3]
    k1 = sol.removeElement(nums1, 3)
    print(f"k = {k1}, nums = {nums1[:k1]}")  # k = 2, nums = [2, 2]
    
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = sol.removeElement(nums2, 2)
    print(f"k = {k2}, nums = {nums2[:k2]}")  # k = 5, nums = [0, 1, 3, 0, 4]
