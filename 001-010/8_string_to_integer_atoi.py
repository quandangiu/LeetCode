class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, n = 0, len(s)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        # 2. Check sign
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # 4. Check for overflow
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1
        return sign * num

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))           # Output: 42
    print(s.myAtoi("   -042"))      # Output: -42
    print(s.myAtoi("1337c0d3"))    # Output: 1337
    print(s.myAtoi("0-1"))          # Output: 0
    print(s.myAtoi("words and 987"))# Output: 0
    print(s.myAtoi("-91283472332")) # Output: -2147483648 (clamped)
    print(s.myAtoi("21474836460"))  # Output: 2147483647 (clamped)
