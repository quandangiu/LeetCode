# 31. Next Permutation
# Difficulty: Medium
# A permutation is a rearrangement of members of a sequence. 
# The next permutation of an array of integers is the next lexicographically greater permutation.

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Test
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 2, 3]
    sol.nextPermutation(nums1)
    print(nums1)  # [1, 3, 2]
    
    nums2 = [3, 2, 1]
    sol.nextPermutation(nums2)
    print(nums2)  # [1, 2, 3]
    
    nums3 = [1, 1, 5]
    sol.nextPermutation(nums3)
    print(nums3)  # [1, 5, 1]
