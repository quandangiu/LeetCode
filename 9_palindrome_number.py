class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10
        return x == reverted or x == reverted // 10

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))   # Output: True
    print(s.isPalindrome(-121))  # Output: False
    print(s.isPalindrome(10))    # Output: False
    print(s.isPalindrome(0))     # Output: True
    print(s.isPalindrome(12321)) # Output: True
