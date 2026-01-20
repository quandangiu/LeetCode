# 45. Jump Game II
# Difficulty: Medium
# You are given a 0-indexed array of integers nums of length n. 
# You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i.
# Return the minimum number of jumps to reach nums[n - 1].

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:
                    break
        
        return jumps


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.jump([2, 3, 1, 1, 4]))  # 2
    print(sol.jump([2, 3, 0, 1, 4]))  # 2
