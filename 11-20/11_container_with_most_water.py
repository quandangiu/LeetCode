class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7])) # Output: 49
    print(s.maxArea([1,1]))                # Output: 1
    print(s.maxArea([4,3,2,1,4]))          # Output: 16
    print(s.maxArea([1,2,1]))              # Output: 2
