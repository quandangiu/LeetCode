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
