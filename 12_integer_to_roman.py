class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
        return roman

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749))  # Output: "MMMDCCXLIX"
    print(s.intToRoman(58))    # Output: "LVIII"
    print(s.intToRoman(1994))  # Output: "MCMXCIV"
    print(s.intToRoman(4))     # Output: "IV"
    print(s.intToRoman(3999))  # Output: "MMMCMXCIX"
