# 29. Divide Two Integers
# Difficulty: Medium
# Given two integers dividend and divisor, divide two integers without using multiplication, 
# division, and mod operator. Return the quotient after dividing dividend by divisor.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Special case for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # Use bit shifting for efficiency
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        return -quotient if negative else quotient


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.divide(10, 3))  # 3
    print(sol.divide(7, -3))  # -2
    print(sol.divide(-2147483648, -1))  # 2147483647 (overflow handled)
