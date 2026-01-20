# 31. Next Permutation
# Difficulty: Medium
# A permutation is a rearrangement of members of a sequence. 
# The next permutation of an array of integers is the next lexicographically greater permutation.

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the smallest element greater than nums[i] from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting at i + 1
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
