# 18. 4Sum (Medium)
# https://leetcode.com/problems/4sum/

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(sol.fourSum([2, 2, 2, 2, 2], 8))       # Output: [[2,2,2,2]]
