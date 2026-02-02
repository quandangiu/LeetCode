class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0
        while x_abs != 0:
            pop = x_abs % 10
            x_abs //= 10
            # Check for overflow before multiplying
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))    # Output: 321
    print(s.reverse(-123))   # Output: -321
    print(s.reverse(120))    # Output: 21
    print(s.reverse(0))      # Output: 0
    print(s.reverse(1534236469)) # Output: 0 (overflow)
