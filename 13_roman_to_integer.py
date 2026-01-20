# 13. Roman to Integer (Easy)
# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result


# Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))      # Output: 3
    print(sol.romanToInt("LVIII"))    # Output: 58
    print(sol.romanToInt("MCMXCIV"))  # Output: 1994
