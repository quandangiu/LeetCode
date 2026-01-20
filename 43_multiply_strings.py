# 43. Multiply Strings
# Difficulty: Medium
# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Multiply digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert to string, skipping leading zeros
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or '0'


# Test
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.multiply("2", "3"))  # "6"
    print(sol.multiply("123", "456"))  # "56088"
    print(sol.multiply("0", "52"))  # "0"
