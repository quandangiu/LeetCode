# 50. Pow(x, n)
# Difficulty: Medium
# Implement pow(x, n), which calculates x raised to the power n.

class Solution:
    def myPow(self, x, n):
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            half = helper(x, n // 2)
            
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            x = 1 / x
            n = -n
        
        return helper(x, n)


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.myPow(2.00000, 10))  # 1024.00000
    print(sol.myPow(2.10000, 3))  # 9.26100
    print(sol.myPow(2.00000, -2))  # 0.25000
