# 29. Divide Two Integers
# Difficulty: Medium
# Given two integers dividend and divisor, divide two integers without using multiplication, 
# division, and mod operator. Return the quotient after dividing dividend by divisor.

class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
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
    print(sol.divide(-2147483648, -1))  # 2147483647
